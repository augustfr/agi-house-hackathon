import openai
from environs import Env
from news_agents.agents.script_agent import ScriptAgent
from news_agents.agents.sorter_agent import SorterAgent
from news_agents.agents.pitch_agent import PitchAgent
from news_agents.agents.judge_agent import JudgeAgent
from news_agents.llms.openai_gpt import OpenAIGPT
from news_agents.workflow.runs import run_main_loop

if __name__ == "__main__":
    env = Env()
    env.read_env()

    OPENAI_API_KEY = env("OPENAI_API_KEY", "")
    OPENAI_TEMPERATURE = env.float("OPENAI_TEMPERATURE", 0.0)
    MAIN_MODEL = env("MAIN_MODEL", "gpt-3.5-turbo").lower()
    openai.api_key = OPENAI_API_KEY

    MAX_TOKENS = env.int("MAX_TOKENS", 4000)

    DEBUG_MODE = env.bool("DEBUG_MODE", False)

    main_lm = OpenAIGPT(
        model=MAIN_MODEL,
        temperature=OPENAI_TEMPERATURE,
    )

    scripter = None
    scripter = ScriptAgent(
        name="scripter",
        language_model=main_lm,
        max_tokens=MAX_TOKENS,
        debug_mode=DEBUG_MODE,
    )

    sorter = None
    sorter = SorterAgent(
        name="sorter",
        language_model=main_lm,
        max_tokens=MAX_TOKENS,
        debug_mode=DEBUG_MODE,
    )

    pitcher = None
    pitcher = PitchAgent(
        name="pitcher",
        language_model=main_lm,
        max_tokens=MAX_TOKENS,
        debug_mode=DEBUG_MODE,
    )

    judge = None
    judge = JudgeAgent(
        name="judge",
        language_model=main_lm,
        max_tokens=MAX_TOKENS,
        debug_mode=DEBUG_MODE,
    )

    try:
        run_main_loop(scripter, sorter, pitcher, judge)
    except Exception as e:
        print(e)
