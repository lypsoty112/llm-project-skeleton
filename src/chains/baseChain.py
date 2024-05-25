from abc import ABC, abstractmethod
from typing import Type

from langchain_core.runnables import Runnable
from pydantic import BaseModel

from src.components.base.baseComponent import BaseComponent
from src.components.llm.baseLlm import BaseLlm
from src.config import Config
from src.models.chains.base import ChainBuildData, OuterChainInput, OuterChainOutput
from src.components.llm import *  # noqa


class BaseChain(BaseComponent, ABC):
    _chain: Runnable | None
    _llm: BaseLlm | None

    def __init__(self, config: Config = None):
        super().__init__(config=config)
        self._chain_config = self.config.get_chain_config(self.__class__.__name__)
        self._chain = None
        self.load_llm()

    @abstractmethod
    def build(self, build_data: ChainBuildData | dict):
        pass

    @abstractmethod
    def run(self, data: Type[BaseModel] | dict) -> BaseModel:
        pass

    @abstractmethod
    async def run_async(self, data: Type[BaseModel] | dict) -> BaseModel:
        pass

    @abstractmethod
    async def stream(self, data: Type[BaseModel] | dict) -> BaseModel:
        pass

    def load_llm(self):
        # Use the config to load the LLM
        self._llm = eval(self._chain_config['llm'])(self.config)

    @property
    def langchain_component(self) -> any:
        return self._chain


class BaseOuterChain(BaseChain, ABC):
    def __init__(self, config: Config = None):
        super().__init__(config=config)

    @abstractmethod
    def run(self, data: OuterChainInput | dict) -> OuterChainOutput:  # NOTE: These types can be changed according to the requirements of your project
        pass

    @abstractmethod
    async def run_async(self, data: OuterChainInput | dict) -> OuterChainOutput:  # NOTE: These types can be changed according to the requirements of your project
        pass

    @abstractmethod
    async def stream(self, data: OuterChainInput | dict):  # NOTE: These types can be changed according to the requirements of your project
        pass
