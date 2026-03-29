import getpass
import os

import dotenv
import dead_parrot as dp  # type: ignore[import-untyped]

dotenv.load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

dmd_assistant: dp.AiAssistant = dp.DspyAiAssistant(
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
        examples=dp.utils.load_dicts_from_json("dataset/x.json"),
    ),
    metrics={
        "recall": dp.metrics.SimpleRecall(judge_model="openai/gpt-4o"),
    },
)

dmd_assistant.ask("What is DMD?")
dmd_assistant.evaluate(metric="recall")
dmd_assistant.optimize(metric="recall", effort="heavy")
dmd_assistant.evaluate(metric="recall")
