from abc import ABC, abstractmethod

from langchain_core.language_models.base import BaseLanguageModel

from src.components.base.baseComponent import BaseComponent
from src.config import Config
from src.models.llm.main import LlmBuildData, LlmChatData, LlmChatResponse, LlmRunData, LlmRunResponse


class BaseLlm(BaseComponent, ABC):
    _llm: BaseLanguageModel

    def __init__(self, config: Config = None) -> None:
        super().__init__(config=config)

    @abstractmethod
    def build(self, build_data: LlmBuildData | dict):
        pass

    @abstractmethod
    def run(self, data: LlmRunData | dict) -> LlmRunResponse:
        pass

    @abstractmethod
    async def run_async(self, data: LlmRunData | dict) -> LlmRunResponse:
        pass

    @abstractmethod
    async def stream(self, data: LlmRunData | dict):
        pass

    @abstractmethod
    def chat(self, data: LlmChatData | dict) -> LlmChatResponse:
        pass

    @abstractmethod
    async def chat_async(self, data: LlmChatData | dict) -> LlmChatResponse:
        pass

    @abstractmethod
    async def chat_stream(self, data: LlmChatData | dict):
        pass

    @property
    def langchain_component(self) -> BaseLanguageModel:
        return self._llm

    def handle_history(self, history: LlmChatData | dict) -> str:
        data = self.handle_input(history, LlmChatData)
        return "\n".join(f"{message['role']}: '{message['content']}'" for message in data["history"])
