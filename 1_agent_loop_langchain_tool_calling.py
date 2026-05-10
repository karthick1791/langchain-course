import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langsmith import traceable

load_dotenv()

MAX_ITERATIONS = 10
ollama_model_name=os.getenv("OOLAMA_MODEL_NAME")


# ---------- Tools -----------
@tool
def get_product_price(product: str) -> float:
    """Tool to get the price of a product"""
    # In a real implementation, this would query a database or an API
    print(f"Getting price for product: {product}")
    prices = {
        "laptop": 999.99,
        "smartphone": 499.99,
        "headphones": 199.99,
    }
    return prices.get(product.lower(), 0)

@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Tool to apply a discount to a price based on the discount tier and return the final price
    Available discount tiers are: bronze, silver, gold"""
    print(f"Applying {discount_tier} discount to price: {price}")
    discount_percentages = {
        "bronze": 10,
        "silver": 20,
        "gold": 30
    }
    discount = discount_percentages.get(discount_tier.lower(), 0) / 100
    return round(price * (1 - discount), 2)

# ---------- Agent Loop -----------
@traceable(name="Langchain agent loop for e-commerce example")
def run_agent(question: str):
    tools = [get_product_price, apply_discount]
    tools_dict = {tool.name: tool for tool in tools}

    llm = init_chat_model(model=f"ollama:{ollama_model_name}", temperature=0)
    llm_with_tools = llm.bind_tools(tools)

    print(f"Running agent loop for question: {question}")

    messages = [
        SystemMessage(
            content=(
                "You are a helpful shopping assistant. "
                "You have access to a product catalog tool "
                "and a discount tool.\n\n"
                "STRICT RULES — you must follow these exactly:\n"
                "1. NEVER guess or assume any product price. "
                "You MUST call get_product_price first to get the real price.\n"
                "2. Only call apply_discount AFTER you have received "
                "a price from get_product_price. Pass the exact price "
                "returned by get_product_price — do NOT pass a made-up number.\n"
                "3. NEVER calculate discounts yourself using math. "
                "Always use the apply_discount tool.\n"
                "4. If the user does not specify a discount tier, "
                "ask them which tier to use — do NOT assume one."
            )
        ),
        HumanMessage(content=question),
    ]

    for i in range(MAX_ITERATIONS):
        print(f"\n--- Agent iteration {i+1} ---")

        #React loop: Thought
        ai_message = llm_with_tools.invoke(messages)
        print(f"Agent response: {ai_message}")

        tool_calls = ai_message.tool_calls
        if not tool_calls:
            print("No tool calls detected. Assuming agent is done.")
            return ai_message.content
        
        #React loop: Action
        tool_call = tool_calls[0]  # Only handle one tool call per iteration for simplicity
        tool_name = tool_call.get("name")
        tool_args = tool_call.get("args", {})
        tool_call_id = tool_call.get("id")  # Unique ID for this tool call, useful for tracing and matching responses
        
        print(f"Detected tool call: {tool_name} with args {tool_args}")
        if tool_name not in tools_dict:
            print(f"Unknown tool: {tool_name}. Ignoring this tool call.")
            continue
        
        tool_func = tools_dict.get(tool_name)
        tool_result = tool_func.invoke(tool_args)
        print(f"Tool result: {tool_result}")
        #React loop: Action
        
        # React loop: Observation
        # This observation along with historical messages is sent back to the agent in the next iteration to inform its next thought and action
        messages.append(ai_message)
        messages.append(ToolMessage(name=tool_name, content=str(tool_result), tool_call_id=tool_call_id)) 
    
    print("ERROR Max iterations reached without agent finishing. Stopping loop.")
    return None

def main():
    print("Hello from e-commerce agent!")
    # ReAct loop : Query
    result = run_agent("What is the final price of a laptop with a gold discount?")
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()