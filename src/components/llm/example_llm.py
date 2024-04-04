from langchain_core.language_models import BaseLanguageModel
from langchain_openai import ChatOpenAI, OpenAI
from src.components.llm.baseLLM import BaseLLM
from src.models.llm import LlmOutput


class ExampleLLM(BaseLLM):
    def __init__(self, chat: bool = False, model_parameters: dict = None) -> None:
        super().__init__(chat, model_parameters)
        self.llm_name = "example-llm"

    def build(self) -> BaseLanguageModel:
        return ChatOpenAI(**self.model_parameters) if self.chat else OpenAI(**self.model_parameters)

    def post_run(self, data: object) -> LlmOutput:
        return LlmOutput(
            completion=str(data),
        )
