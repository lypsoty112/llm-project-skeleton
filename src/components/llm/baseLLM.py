from langchain_core.language_models.base import BaseLanguageModel

from src.components.base.baseComponent import BaseComponent
from src.models.llm import LlmOutput


class BaseLLM(BaseComponent):
    def __init__(self, chat: bool = False, model_parameters: dict = None) -> None:
        """
        Constructs a BaseLLM object. This class is meant to be subclassed by all LLMs.
        :param chat: Whether the LLM is a chat model or not. Not always an option.
        :param model_parameters: The parameters to pass to the LLM.
        """
        super().__init__()
        if model_parameters is None:
            model_parameters = {}

        self.chat: bool = chat  # Whether the LLM is a chat model or not. Not always an option.
        self.model_parameters: dict = model_parameters  # The parameters to pass to the LLM.
        self.llm_name: str = "base-llm"  # The name of the LLM. Useful for debugging.

    def build(self) -> BaseLanguageModel:
        return BaseLanguageModel(
            **self.model_parameters
        )

    def post_run(self, data: object) -> LlmOutput:
        return LlmOutput(
            completion=str(data),
        )
