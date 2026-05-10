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

def main():
    print("Hello from e-commerce agent!")
    result = run_agent("What is the final price of a laptop with a gold discount?")
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()