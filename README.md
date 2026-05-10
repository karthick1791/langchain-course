# LangChain Course

This repository contains LangChain experiments that demonstrate local and cloud model integration, prompt templates, and tool-based agents.

## Project Structure

- `mainLlmIntegration.py` - prompt template integration with Ollama or OpenAI
- `mainSearchAgent.py` - tool-enabled search agent example using Tavily search
- `1_agent_loop_langchain_tool_calling.py` - ReAct-style agent loop example with product pricing and discount tools
- `docs/` - detailed documentation for each script
- `pyproject.toml` - project dependencies and packaging
- `.env` - environment configuration (not checked in)

## Getting Started

1. Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -e .
```

3. Configure environment variables in a `.env` file.

## Documentation

- [mainLlmIntegration](docs/mainLlmIntegration.md)
- [mainSearchAgent](docs/mainSearchAgent.md)
- [1_agent_loop_langchain_tool_calling](docs/1_agent_loop_langchain_tool_calling_react_loop.md)
- [2_agent_loop_raw_function_calling](docs/2_agent_loop_raw_function_calling.md)

## Custom Agent

Use the custom agent `/create-docs-for-python` to generate or refresh `docs/*.md` files for executable Python scripts and keep `README.md` updated with links to those docs.

## Environment Configuration

Create a `.env` file with the model and API settings you want to use. Example:

```env
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
OOLAMA_MODEL_NAME=llama3
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=gpt-4o
TAVILY_API_KEY=your-tavily-api-key
```

## Execution

Run any script using Python module mode, for example:

```bash
python -m mainLlmIntegration
python -m mainSearchAgent
python -m 1_agent_loop_langchain_tool_calling
python -m 2_agent_loop_raw_function_calling
```

## Notes

- `temperature=0` is used for consistent outputs in examples.
- `docs/` contains per-script details and execution steps.

## License

Add license information here.
