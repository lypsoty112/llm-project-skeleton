import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class Message(BaseModel):
    content: str = Field(..., description="Content of the message", example="Hello, how are you?")
    role: Literal["human", "ai", "system"] = Field(..., description="Role of the entity sending the message", example="human")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)


class History(BaseModel):
    messages: list[Message] = Field([], description="List of messages in the conversation, sorted from earliest to newest.")

    def __init_subclass__(cls, **kwargs: ConfigDict):
        # Sort messages by timestamp
        cls.messages = sorted(cls.messages, key=lambda x: x.timestamp)
        return super().__init_subclass__(**kwargs)
