import getpass
import os

import dotenv
import dead_parrot as dp

dotenv.load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

ecb_ai_assistant: dp.AiAssistant = dp.DspyAiAssistant(
    lm="openai/gpt-4o-mini",
    embedder="openai/text-embedding-3-small",
    corpus=dp.utils.load_corpus_from_pdf(
        "DMD",
        "context/dmd.pdf",
    ),
    examples=dp.utils.load_examples_from_json("examples/x.json"),
)
print(ecb_ai_assistant.ask("what is data processing cycle? And how many stages are there in it?"))

