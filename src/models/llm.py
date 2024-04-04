from pydantic import BaseModel, Field
from typing import Optional

"""
This file contains the Pydantic models for the LLM components.
"""


class LlmInput(BaseModel):
    prompt: str = Field(..., description="The prompt to be sent to the LLM.")
    metadata: dict = Field(description="The metadata to be sent to the LLM.", default={})


class LlmOutput(BaseModel):
    completion: str = Field(..., description="The completion from the LLM.")
    cost: int = Field(description="The number of tokens used in the completion.",
                      default=0,
                      ge=0)
    time_to_complete: float = Field(description="The time taken to generate the completion.",
                                    default=0.0,
                                    ge=0.0)
    metadata: dict = Field(description="The metadata from the LLM.", default={})
    input: Optional[LlmInput] = Field(..., description="The input to the LLM.")
