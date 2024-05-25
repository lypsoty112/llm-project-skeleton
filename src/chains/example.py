from langchain_core.prompts import PromptTemplate
from loguru import logger

from src.chains.baseChain import BaseOuterChain
from src.config import Config
from src.models.chains.base import ChainBuildData, OuterChainInput, OuterChainOutput
from src.models.main import Message

PROMPT = "Respond to the following message as sarcastically as possible: {message}"


class SarcasticChain(BaseOuterChain):
    def __init__(self, config: Config = None):
        super().__init__(config=config)

    def build(self, build_data: ChainBuildData | dict):
        promptTemplate = PromptTemplate(input_types={"message": str}, input_variables=["message"], template=PROMPT)
        self._llm.build({"chat": True})
        self._chain = promptTemplate | self._llm.langchain_component

    def run(self, data: OuterChainInput | dict) -> OuterChainOutput:
        logger.info(f"Running SarcasticChain with data: {data}")
        # Get the last message from the history
        last_message = data['history'][-1]['content']
        response = self._chain.invoke({"message": last_message})
        return OuterChainOutput(message=Message(content=response.content, role="ai"), metadata=response.response_metadata)

    async def run_async(self, data: OuterChainInput | dict) -> OuterChainOutput:
        logger.info(f"Running SarcasticChain with data: {data}")
        last_message = data['history'][-1]['content']
        response = await self._chain.ainvoke({"message": last_message})
        return OuterChainOutput(message=Message(content=response.content, role="ai"), metadata=response.response_metadata)

    async def stream(self, data: OuterChainInput | dict):
        raise NotImplementedError
