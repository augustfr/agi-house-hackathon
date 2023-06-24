from typing import List, Union, Callable
import openai
from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env("OPENAI_API_KEY", "")
openai.api_key = OPENAI_API_KEY


def call(
    model,
    temperature,
    messages,
    functions: List[Callable],
    function_call,
    stop_string: Union[None, str] = None,
):
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=messages,
        functions=functions,
        function_call=function_call,
        stop=stop_string,
    )
    return completion
