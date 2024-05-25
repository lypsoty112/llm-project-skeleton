from pydantic import BaseModel, Field
from src.models.main import History, Message


class LlmBuildData(BaseModel):
    chat: bool = Field(False, description="Whether the model is a chat model")
    temperature: float = Field(0.7, description="Temperature. Might be ignored.")
    max_tokens: int = Field(1024, description="Maximum output tokens. Might be ignored.")
    streaming: bool = Field(False, description="Whether the model should be streaming the output. Might be ignored.")
    max_retries: int = Field(1, description="Maximum retries. Might be ignored.")


class LlmRunData(BaseModel):
    text: str = Field(..., description="Text to be processed")


class LlmRunResponse(BaseModel):
    text: str = Field(..., description="Generated text")


class LlmChatData(BaseModel):
    history: History = Field(..., description="Conversation history")


class LlmChatResponse(BaseModel):
    message: Message = Field(..., description="Generated message")
