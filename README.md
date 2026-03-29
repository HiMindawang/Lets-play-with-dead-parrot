# lets-play-with-dead-parrot
All my love to pygumby

## How to use

1. Add your PDF to `context/` and examples to `examples/` (JSON file with `question`/`answer` keys, min 4 entries)
2. Set `OPENAI_API_KEY` in a `.env` file (or enter it when prompted)
3. Run `uv run main.py`

## How it works

Uses [dead-parrot](https://pypi.org/project/dead-parrot/) to build a DSPy-powered RAG assistant:

```python
assistant = dp.DspyAiAssistant(
    name="DMD",
    models=dp.Models(
        task="openai/gpt-4o-mini",
        teacher="openai/gpt-4o",
        embedding="openai/text-embedding-3-small",
    ),
    corpus=dp.Corpus(
        name="DMD",
        texts=dp.utils.load_pages_from_pdf("context/dmd.pdf"),
    ),
    dataset=dp.Dataset(
        examples=dp.utils.load_dicts_from_json("examples/x.json"),
    ),
    metrics={
        "recall": dp.metrics.SimpleRecall(judge_model="openai/gpt-4o"),
    },
)

assistant.evaluate(metric="recall")       # eval on devset
assistant.optimize(metric="recall", effort="heavy")  # optimise with MIPROv2
assistant.evaluate(metric="recall")       # re-eval after optimisation
```

## Development

```bash
uv add <package>        # add a dependency
uv run mypy main.py     # type-check
uv run main.py          # run
```
