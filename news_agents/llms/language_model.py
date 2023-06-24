from abc import ABC, abstractmethod
from typing import Union


class LanguageModel(ABC):
    @abstractmethod
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature

    @abstractmethod
    def call(
        self,
        messages,
        functions,
        function_call,
        stop_string: Union[None, str] = None,
    ):
        pass
