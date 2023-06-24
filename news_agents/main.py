import openai
from environs import Env
from news_agents.agents.summarizer_agent import SummarizerAgent
from news_agents.llms.openai_gpt import OpenAIGPT

if __name__ == "__main__":
    env = Env()
    env.read_env()

    OPENAI_API_KEY = env("OPENAI_API_KEY", "")
    OPENAI_TEMPERATURE = env.float("OPENAI_TEMPERATURE", 0.0)
    MAIN_MODEL = env("MAIN_MODEL", "gpt-3.5-turbo").lower()
    openai.api_key = OPENAI_API_KEY

    MAX_TOKENS = env.int("MAX_TOKENS", 4000)

    main_lm = OpenAIGPT(
        model=MAIN_MODEL,
        temperature=OPENAI_TEMPERATURE,
    )

    summarizer = None
    summarizer = SummarizerAgent(
        name="summarizer",
        language_model=main_lm,
        max_tokens=MAX_TOKENS,
        debug_mode=True,
    )

    try:
        run_main_loop(
            summarizer,
        )
    except Exception as e:
        print(e)
