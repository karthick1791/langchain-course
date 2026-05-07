# LangChain Course

A learning project demonstrating LangChain usage with different LLM backends for text summarization, fact extraction, and agent-based search.

## Overview

This repository contains two main Python experiments:

- `mainLlmIntegration.py`: Uses LangChain prompt templates and integrates with either Ollama or OpenAI to summarize a biography and extract interesting facts.
- `mainSearchAgent.py`: Experiments with a tool-enabled agent using Ollama and a search function stub, plus an optional Tavily search helper.

## Features

- **Flexible LLM Support**: Switches between local Ollama and cloud OpenAI based on environment configuration
- **Prompt Templates**: Uses LangChain's `PromptTemplate` for structured prompt engineering
- **Agent Tools**: Demonstrates LangChain agent creation and tool invocation
- **Environment Configuration**: Loads configuration from `.env` using `python-dotenv`

## Prerequisites

- Python 3.14+
- pip or package manager

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain-course
```

2. Install dependencies:
```bash
pip install -e .
```

This will install all packages listed in `pyproject.toml`:
- `langchain`
- `langchain-openai`
- `langchain-ollama`
- `langchain-core`
- `python-dotenv`
- `black` (code formatter)
- `isort` (import sorter)

## Configuration

### Environment Variables

Create a `.env` file in the project root with one or more of these variables:

```env
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
OOLAMA_MODEL_NAME=llama3
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL_NAME=gpt-4o
```

- If `OLLAMA_LOCAL_ENDPOINT` is set, `mainLlmIntegration.py` and `mainSearchAgent.py` will use Ollama.
- Otherwise, `mainLlmIntegration.py` falls back to OpenAI if `OPENAI_API_KEY` is provided.

### Setting Up Ollama (Optional)

To use the local Ollama backend:

1. Install Ollama from https://ollama.ai
2. Pull the llama3 model:
   ```bash
   ollama pull llama3
   ```
3. Start the Ollama server:
   ```bash
   ollama serve
   ```

## Usage

Run the integration script:

```bash
python -m mainLlmIntegration
```

Run the search agent experiment:

```bash
python -m mainSearchAgent
```

## File Descriptions

### `mainLlmIntegration.py`

- Loads environment settings with `python-dotenv`
- Builds a prompt template for summarizing a biography and extracting two interesting facts
- Selects either `ChatOllama` or `ChatOpenAI` depending on configuration
- Invokes the prompt chain and prints the LLM response

### `mainSearchAgent.py`

- Defines a simple LangChain tool named `search`
- Uses `create_agent` to build an agent with Ollama as the model backend
- Demonstrates invoking the agent with a human query about Tamil Nadu elections
- Includes a `search_web` helper using `TavilyClient` for optional web search integration

## Project Structure

```
langchain-course/
├── mainLlmIntegration.py   # LLM integration experiment with prompt templates
├── mainSearchAgent.py      # Agent + tool experiment using Ollama and search
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # This file
└── .env                    # Environment variables (create this file)
```

## How It Works

### `mainLlmIntegration.py`

- Uses a `PromptTemplate` to structure the request
- Chooses between Ollama and OpenAI models
- Runs a prompt chain and prints the formatted output

### `mainSearchAgent.py`

- Registers a tool for search queries
- Creates an agent that can call the tool
- Sends a user prompt to the agent and prints the result

## Dependencies

See `pyproject.toml` for the complete list of dependencies:

- **langchain**: Core LangChain framework
- **langchain-openai**: OpenAI integration
- **langchain-ollama**: Ollama integration
- **python-dotenv**: Environment variable management
- **black**: Code formatting
- **isort**: Import organization

## Troubleshooting

### ImportError: No module named 'dotenv'
Ensure dependencies are installed:
```bash
pip install -e .
```

### Pylance warnings about imports
Make sure Pylance is configured to use your project's virtual environment:
- Use `.venv/Scripts/python.exe` as the Python interpreter

### Connection refused when using Ollama
Ensure the Ollama server is running:
```bash
ollama serve
```

### OpenAI API errors
Verify that your `OPENAI_API_KEY` is correct and has sufficient quota.

## Development

This project uses:
- **black** for code formatting
- **isort** for import organization

Run these tools:
```bash
black .
isort .
```

## Future Enhancements

- Support for additional LLM models
- Batch processing of multiple biographies
- Customizable prompt templates
- Output formatting options
- Integration with additional data sources

## License

Add appropriate license information here.

## Notes

The `temperature=0` setting used in the scripts ensures deterministic, consistent outputs for reproducibility.
