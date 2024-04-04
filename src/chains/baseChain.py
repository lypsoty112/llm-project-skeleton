from langchain_core.runnables import Runnable

from src.components.llm.baseLLM import BaseLLM
from src.components.base.baseComponent import BaseComponent


class BaseChain(BaseComponent):
    def __init__(self):
        super().__init__()
        self.llm_name: str = ""  # The name of the LLM that this chain uses. Useful for debugging
        self.chain_name: str = ""  # The name of the chain. Useful for debugging
        self.prompt: str = ""  # The prompt that the chain uses to generate completions
        self._llm: BaseLLM | None = None  # The LLM that the chain uses
        self._chain: Runnable | None = None  # The chain that the chain uses. This is created in the build method

    def build(self) -> None:
        """
        Builds the chain internally. This method should be called before running the chain.
        The reason this is not done in the constructor is to allow for more flexibility in the chain's construction.
        :return:
        """
        return None

    def run(self, data: object) -> object:
        """
        Runs the chain on the given data and returns the result.
        :param data: The data to run the chain on
        :return: The result of running the chain
        """
        assert self._chain is not None, "Chain not built"
        data = self.pre_run(data)
        response = self._chain.invoke(data)
        response = self.post_run(response)
        return response

    async def run_async(self, data: object) -> object:
        """
        Runs the chain on the given data and returns the result.
        :param data: The data to run the chain on
        :return: The result of running the chain
        """
        assert self._chain is not None, "Chain not built"
        data = self.pre_run(data)
        response = self._chain.ainvoke(data)
        response = self.post_run(response)
        return response

    def pre_run(self, data: object) -> object:
        """
        Preprocesses the data before running the chain. This method should only be called in the run method.
        :param data:
        :return:
        """
        assert self._chain is not None, "Chain not built"
        return data

    def post_run(self, data: object) -> object:
        """
        Post-processes the data after running the chain. This method should only be called in the run method.
        :param data:
        :return:
        """
        assert self._chain is not None, "Chain not built"
        return data

    def __str__(self) -> str:
        return f"{self.chain_name} using {self.llm_name}"
