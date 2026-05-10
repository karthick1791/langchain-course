# mainLlmIntegration.py

## What this file does

This script demonstrates basic LangChain integration with prompt templates and multiple LLM backends.

It:

- Loads environment variables via `python-dotenv`.
- Creates a `PromptTemplate` for summarizing a biography and extracting two interesting facts.
- Uses either the Ollama or OpenAI chat model depending on environment configuration.
- Executes the prompt chain and prints the model response.

## Key behavior

- If `OLLAMA_LOCAL_ENDPOINT` is defined, the script uses `ChatOllama`.
- Otherwise, it uses `ChatOpenAI` and relies on `OPENAI_API_KEY`.
- The `temperature` is set to `0` for deterministic output in this example.

## Execution steps

1. Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

2. Configure `.env` with values such as:

```env
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
OOLAMA_MODEL_NAME=llama3
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=gpt-4o
```

3. Run the script:

```bash
python -m mainLlmIntegration
```

4. The script prints the model’s response, which includes a short summary and two interesting facts about the subject.

## Notes

- This file is useful for testing prompt chaining with different LLM backends.
- The biography text is hard-coded and can be replaced with any other information source for experimentation.
