import sys

from loguru import logger

from src.chains.baseChain import BaseOuterChain
from src.config import Config
from src.models.chains.base import OuterChainInput, OuterChainOutput
from src.chains import * # noqa


class Controller:
    main_chain: BaseOuterChain

    def __init__(self):
        # Get the config
        self.config = Config()
        logging_config = self.config.get_property("LOG_CONFIGS")
        logger.remove()

        terminal_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <cyan>{file}:{line}</cyan> <level>{level:>8}</level> {message}"
        logger.add(sys.stdout, format=terminal_format, level=logging_config["level"], colorize=True)
        # Add a file sink to log to a file
        if logging_config["file"]:
            logger.add(logging_config["file"], format="{time} {level} {message}", level=logging_config["level"])

        # Load the main chain
        try:
            main_chain = self.config.get_property("main_chain")
            assert isinstance(main_chain, str), "Main chain must be a string"
            self.main_chain = eval(main_chain)(self.config)
            assert isinstance(self.main_chain, BaseOuterChain), "Main chain must be an instance of BaseOuterChain"
        except Exception as e:
            logger.exception(f"Error loading main chain: {e}")
            exit(-1)

        self.main_chain.build({})


    def run(self, data: OuterChainInput | dict) -> OuterChainOutput:
        return self.main_chain.run(data)

    async def run_async(self, data: OuterChainInput | dict) -> OuterChainOutput:
        return await self.main_chain.run_async(data)

    async def stream(self, data: OuterChainInput | dict):
        raise NotImplementedError
