import os

from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

def get_ollama_llm():
    return ChatOllama(model="llama3", temperature=0, base_url=os.getenv("OLLAMA_LOCAL_ENDPOINT"))

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:        query (str): The search query
    Returns:     str: The search results
    """
    return "May be TVK wil form the Govt"

def search_web(query: str) -> str:
    client = TavilyClient("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")
    response = client.search(
    query=query,
    search_depth="advanced"
    )
    return response


def main():
    print("Hello from search agent!")
    #(search_web("What are the latest updates on Tamil Nadu elections?"))
    
    llm = get_ollama_llm()
    tools = [search]
    agent = create_agent(model=llm, tools=tools)

    result = agent.invoke(HumanMessage(content="What are the latest updates on Tamil Nadu elections?"))
    print(result.content)


# File "C:\Users\Karthick\git\langchain-course\.venv\Lib\site-packages\ollama\_client.py", line 189, in inner
#    raise ResponseError(e.response.text, e.response.status_code) from None
#ollama._types.ResponseError: registry.ollama.ai/library/llama3:latest does not support tools (status code: 400)

# switch to gpt-oss or upgrade to latest version llama3.1 + to get tool support

if __name__ == "__main__":
    main()
