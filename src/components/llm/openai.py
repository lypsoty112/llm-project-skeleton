from langchain_openai import OpenAI, ChatOpenAI

from src.components.llm.baseLlm import BaseLlm
from src.config import Config
from src.models.llm.main import LlmBuildData, LlmChatData, LlmChatResponse, LlmRunData, LlmRunResponse
from src.models.main import Message


class Gpt35(BaseLlm):

    def __init__(self, config: Config = None) -> None:
        super().__init__(config=config)

    def build(self, build_data: LlmBuildData | dict):
        build_data = self.handle_input(build_data, LlmBuildData)
        if build_data["chat"]:
            self._llm = ChatOpenAI(temperature=build_data["temperature"], max_tokens=build_data["max_tokens"], streaming=build_data["streaming"], max_retries=build_data["max_retries"])
        else:
            self._llm = OpenAI(temperature=build_data["temperature"], max_tokens=build_data["max_tokens"], streaming=build_data["streaming"], max_retries=build_data["max_retries"])

    def run(self, data: LlmRunData | dict) -> LlmRunResponse:
        data = self.handle_input(data, LlmRunData)
        response = self._llm.invoke(data["text"])
        return LlmRunResponse(text=response)

    async def run_async(self, data: LlmRunData | dict) -> LlmRunResponse:
        data = self.handle_input(data, LlmRunData)
        response = await self._llm.ainvoke(data["text"])
        return LlmRunResponse(text=response)

    async def stream(self, data: LlmRunData | dict):
        raise NotImplementedError

    def chat(self, data: LlmChatData | dict) -> LlmChatResponse:
        data = self.handle_history(data)
        response = self.run({"text": data})
        return LlmChatResponse(text=response)

    async def chat_async(self, data: LlmChatData | dict) -> LlmChatResponse:
        data = self.handle_history(data)
        response = await self.run_async({"text": data})
        return LlmChatResponse(text=response)

    async def chat_stream(self, data: LlmChatData | dict):
        raise NotImplementedError
