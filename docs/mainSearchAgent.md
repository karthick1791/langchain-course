# mainSearchAgent.py

## What this file does

This script demonstrates a tool-enabled LangChain search agent using the Tavily search integration.

It:

- Loads environment variables with `python-dotenv`.
- Defines an `AgentResponse` Pydantic schema to structure the output.
- Creates an Ollama chat model with `ChatOllama`.
- Builds a LangChain agent using `create_agent(...)`.
- Uses `TavilySearch()` as a tool to perform external search queries.

## Key behavior

- The agent is configured to accept `HumanMessage` input and return structured results.
- The script includes an alternate direct `@tool` wrapper around `TavilyClient` for custom search tooling.
- The main run example asks the agent: `When was Taj Mahal built?`

## Execution steps

1. Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

2. Configure `.env` with at least:

```env
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
OOLAMA_MODEL_NAME=llama3
TAVILY_API_KEY=your-tavily-api-key
```

3. Run the script:

```bash
python -m mainSearchAgent
```

4. The script prints the agent result, which should include answer content and sources if the tool and model successfully return structured output.

## Notes

- Local model behavior may vary and may not always populate the `AgentResponse` structured fields.
- The script is intended as an experimental example of combining LangChain agents with search tooling.
