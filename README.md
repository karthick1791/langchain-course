# LangChain Course

A learning project demonstrating LangChain usage with different LLM backends for text summarization and fact extraction.

## Overview

This project showcases how to use LangChain to build an AI-powered text processing pipeline. It takes biographical information as input and uses an LLM to:

1. Generate a short summary
2. Extract 2 interesting facts about the person

## Features

- **Flexible LLM Support**: Automatically switches between local (Ollama) and cloud-based (OpenAI) LLMs
- **Prompt Templates**: Uses LangChain's `PromptTemplate` for structured prompt engineering
- **Environment Configuration**: Loads configuration from `.env` file using `python-dotenv`

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

Create a `.env` file in the project root with the following variables:

#### Option 1: Use Local Ollama (Recommended for Development)
```env
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
```

#### Option 2: Use OpenAI
```env
OPENAI_API_KEY=your-openai-api-key-here
```

**Note**: If `OLLAMA_LOCAL_ENDPOINT` is set, the application will use Ollama. Otherwise, it falls back to OpenAI.

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

Run the application:

```bash
python -m main
```

The script will:
1. Load the `.env` file
2. Determine which LLM to use based on environment variables
3. Create a prompt template for summarization and fact extraction
4. Process sample biographical data (Elon Musk) using the selected LLM
5. Print the generated summary and facts

## Project Structure

```
langchain-course/
├── main.py              # Main application script
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
└── .env                 # Environment variables (create this file)
```

## How It Works

### LLM Selection Logic

```python
if OLLAMA_LOCAL_ENDPOINT is set:
    Use ChatOllama with llama3 model
else:
    Use ChatOpenAI with gpt-4o model
```

### Processing Pipeline

1. **Prompt Template**: Defines the structure of the request to the LLM
2. **Chain**: Connects the prompt template to the selected LLM
3. **Invocation**: Processes the input and returns the LLM response

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

The `temperature=0` setting used for both LLMs ensures deterministic, consistent outputs for reproducibility.
