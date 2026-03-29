# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the main application
uv run main.py

# Add a dependency
uv add <package_name>

# Type checking
uv run mypy .
```

## Architecture

This project builds and optimizes a DSPy-based AI assistant using the `dead-parrot` framework. The core flow in `main.py`:

1. A `DspyAiAssistant` is created with separate models for task execution (`gpt-4o-mini`), optimization/teaching (`gpt-4o`), and embeddings (`text-embedding-3-small`).
2. A PDF knowledge base (`context/dmd.pdf`) is used as the RAG corpus.
3. Training examples (`examples/x.json`) are Q&A pairs from the knowledge base.
4. A custom metric function evaluates answer quality using DSPy's `ChainOfThought`.
5. The assistant is queried, then optimized via the dead-parrot framework.

The `dmd/` and `dmd_assistant_____/` directories contain generated embeddings and RAG cache — these are not committed to git.

## Environment

Requires a `.env` file with `OPENAI_API_KEY`. Python 3.13 is specified in `.python-version`.
