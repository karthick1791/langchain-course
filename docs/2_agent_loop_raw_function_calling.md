# 2_agent_loop_raw_function_calling.py

## What this file does

This script demonstrates a raw function-calling agent loop using Ollama without LangChain's higher-level `@tool` integration.

Key behaviors:

- Defines two traced tool functions manually:
  - `get_product_price(product: str)`
  - `apply_discount(price: float, discount_tier: str)`
- Builds explicit JSON schemas for each function in `tools_for_llm`.
- Uses `ollama.chat(...)` directly to invoke the model with tool definitions.
- Implements a loop that inspects the model response for `tool_calls` and executes the first tool call each iteration.
- Appends the agent message and the tool observation back into the conversation history until a final answer is produced.

## Main components

- `@traceable(run_type="tool")` is used for tracing tool functions.
- `tools_for_llm` contains manual function metadata and parameter schemas.
- `ollama_chat_traced(messages)` wraps the `ollama.chat(...)` call with tracing.
- `run_agent(question: str)` is the main loop:
  - sends a system prompt and user question to the model
  - detects a tool call
  - executes the selected tool
  - appends the result and repeats

## How it differs from `1_agent_loop_langchain_tool_calling.py`

- This file does not use LangChain's `llm.bind_tools(...)` interface.
- It manually defines the function call schema that the LLM uses to decide between tools.
- It directly calls `ollama.chat()` instead of a LangChain chat model wrapper.
- It performs direct Python function invocations for the tool result instead of using `tool.invoke()`.

## Execution steps

1. Activate the virtual environment:

```bash
.\.venv\Scripts\activate
```

2. Ensure your `.env` file contains the required settings, for example:

```env
OOLAMA_MODEL_NAME=llama3
OLLAMA_LOCAL_ENDPOINT=http://localhost:11434
```

3. Run the script:

```bash
python -m 2_agent_loop_raw_function_calling
```

4. Observe the printed output for each iteration, tool selection, tool result, and final answer.

## Notes

- This script is best for understanding how raw function calling works with Ollama and how LangChain automates much of this schema generation.
- Because it is a manual implementation, the function metadata is explicit and can be inspected or modified directly.
- It is intentionally limited to one tool call per iteration for clarity.
