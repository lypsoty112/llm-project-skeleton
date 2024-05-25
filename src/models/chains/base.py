from pydantic import BaseModel, Field

from src.models.main import History, Message


class OuterChainInput(BaseModel):
    history: History


class OuterChainOutput(BaseModel):
    message: Message
    metadata: dict = Field({})


class ChainBuildData(BaseModel):
    pass
