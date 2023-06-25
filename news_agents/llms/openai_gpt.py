import openai
from typing import List, Union, Callable
from news_agents.llms.language_model import LanguageModel
import tiktoken
from environs import Env

env = Env()
env.read_env()

enc = tiktoken.encoding_for_model("text-davinci-003")
MAX_TOKENS = env.int("MAX_TOKENS", 4000)


class OpenAIGPT(LanguageModel):
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature

    def message_token_count(self, msg) -> int:
        return len(enc.encode(msg["content"]))

    def call(
        self,
        messages,
        functions: List[Callable],
        function_call,
        stop_string: Union[None, str] = None,
    ):
        total_tokens = sum(self.message_token_count(msg) for msg in messages)
        while total_tokens > MAX_TOKENS:
            removed_message = False
            for i, msg in enumerate(messages):
                if msg["role"] != "system":
                    total_tokens -= self.message_token_count(msg)
                    messages.pop(i)
                    removed_message = True
                    break

            if not removed_message:
                break
        completion = openai.ChatCompletion.create(
            model=self.model,
            temperature=self.temperature,
            messages=messages,
            functions=functions,
            function_call=function_call,
            stop=stop_string,
        )
        return completion
