from abc import ABC, abstractmethod
from typing import Type

from loguru import logger
from pydantic import BaseModel

from src.config import Config


class BaseComponent(ABC):
    config: Config

    def __init__(self, config: Config = None) -> None:
        super().__init__()
        self.config = config
        if config is None:
            logger.warning("No config provided, using default config")
            self.config = Config()

    @abstractmethod
    def build(self, build_data: Type[BaseModel] | dict):
        pass

    @abstractmethod
    def run(self, data: Type[BaseModel] | dict) -> BaseModel:
        pass

    @abstractmethod
    async def run_async(self, data: Type[BaseModel] | dict) -> BaseModel:
        pass

    @staticmethod
    def handle_input(data: Type[BaseModel] | dict, expected: Type[BaseModel]) -> dict:
        if isinstance(data, dict):
            data = expected(**data)
        return data.model_dump()

    @staticmethod
    def handle_output(data: dict, expected: Type[BaseModel]) -> BaseModel:
        return expected(**data)

    @property
    def langchain_component(self) -> any:
        return None
