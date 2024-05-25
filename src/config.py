import os
from typing import Literal

import yaml
from pydantic import Field, BaseModel
from dotenv import load_dotenv


class ChainConfig(BaseModel):
    name: str = Field("default", title="The name of the chain")
    llm: str = Field("Gpt35", title="The exact name of the llm component to be used. Case-sensitive.")


class LogConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field("INFO", title="The log level to be used")
    file: str | None = Field(None, title="The file to write the logs to")


class ConfigModel(BaseModel):
    MAIN_CHAIN: str = Field(..., title="The chain to be used as the main chain")
    CHAIN_CONFIGS: list[ChainConfig] = Field([], title="The configurations of the chains to be used in the main chain. Use 'default' as the name for default configurations.")
    LOG_CONFIGS: LogConfig = Field(LogConfig(), title="The log configuration to be used")


class Config:
    def __init__(self):
        load_dotenv(override=True)
        # Get the correct config file
        # Check for command line arguments
        if "CONFIG_FILE" in os.environ:
            config_file = os.environ["CONFIG_FILE"]
        else:
            # Check in the environment variables
            config_file = os.getenv("CONFIG_FILE", "./configuration/default.yml")

        # Load the yaml file if it exists
        assert os.path.exists(config_file), f"Config file {config_file} not found"
        # Load the yaml file
        config_dict = yaml.safe_load(open(config_file))
        # Parse the config
        self.config: dict = ConfigModel(**config_dict).model_dump()
        # Bring all dict keys lowercase
        self.config = {k.lower(): v for k, v in self.config.items()}

    def get_property(self, property_name) -> str | dict | list | None:
        return self.config[property_name.lower()]

    def get_chain_config(self, chain_name) -> dict | None:
        configuration = next((x for x in self.config["chain_configs"] if x["name"].lower() == chain_name.lower()), None)
        if configuration:
            return configuration

        # Check if there's a default configuration
        return next((x for x in self.config["chain_configs"] if x["name"].lower() == "default"), ChainConfig().model_dump())
