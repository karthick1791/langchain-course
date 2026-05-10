import os

from dotenv import load_dotenv

load_dotenv()

from tavily import TavilyClient
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

from typing import List
from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )


ollama_model_name = os.getenv("OOLAMA_MODEL_NAME")
ollama_endpoint = os.getenv("OLLAMA_LOCAL_ENDPOINT")
tavily_api_key = os.getenv("TAVILY_API_KEY")


def get_ollama_llm():
    return ChatOllama(
        model=ollama_model_name,
        temperature=0,
        base_url=ollama_endpoint,
        streaming=False,
    )


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:        query (str): The search query
    Returns:     str: The search results
    """
    client = TavilyClient(api_key=tavily_api_key)
    print(f"Searching for: {query} using Tavily API")
    response = client.search(query=query)
    return response


def main():
    print("Hello from search agent!")

    llm = get_ollama_llm()
    tools = [
        TavilySearch()
    ]  # using langChain wrapper for Tavily Search as a tool in the agent, this helps adding right parameters to the Tavily API
    # tools = [search] # using the search tool which is a direct wrapper over TavilyClient, this requires us to handle the parameters
    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

    # Note - observation with running local models is that the result object won't have a structured_response field as it couldn't parse the response into AgentResponse format
    # as we mentioned! But cloud models do provide this support, limitations of local models causing it to ignore the response format and just return plain text

    result = agent.invoke(
        {"messages": [HumanMessage(content="When was Taj Mahal built?")]}
    )
    print(result)


if __name__ == "__main__":
    main()
