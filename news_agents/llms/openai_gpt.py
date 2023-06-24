import openai
from typing import List, Union, Callable
from news_agents.llms.language_model import LanguageModel


class OpenAIGPT(LanguageModel):
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature

    def call(
        self,
        messages,
        functions: List[Callable],
        function_call,
        stop_string: Union[None, str] = None,
    ):
        completion = openai.ChatCompletion.create(
            model=self.model,
            temperature=self.temperature,
            messages=messages,
            functions=functions,
            function_call=function_call,
            stop=stop_string,
        )
        return completion
