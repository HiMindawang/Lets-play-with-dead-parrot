import getpass
import os

import dotenv
import dead_parrot as dp  # type: ignore[import-untyped]

dotenv.load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

recall_metric = dp.metrics.SimpleRecall(judge_model="openai/gpt-4o")

dmd_assistant: dp.AiAssistant = dp.DspyAiAssistant(
    name="DMD",
    models=dp.Models(
        task="openai/gpt-4o-mini",
        teacher="openai/gpt-4o",
        embedding="openai/text-embedding-3-small",
    ),
    corpus=dp.Document(
        name="DMD",
        pages=dp.utils.load_pdf("context/dmd.pdf"),
    ),
    dataset=dp.Examples(
        qa_pairs=dp.utils.load_json("examples/dmd.json"),
    ),
    metrics={"recall": recall_metric},
)

dmd_assistant.ask("What is Data Management?")
dmd_assistant.evaluate(metric="recall")
dmd_assistant.optimize(metric="recall", effort="light")
#dmd_assistant.evaluate(metric=recall_metric)
