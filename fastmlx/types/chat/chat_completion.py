from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field


class FunctionCall(BaseModel):
    name: str
    arguments: str


class ToolCall(BaseModel):
    id: str
    type: str = "function"
    function: FunctionCall


class Function(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]


class ChatCompletionContentPartParam(BaseModel):
    type: Literal["text", "image_url"]
    text: str = None
    image_url: dict = None


class ChatMessage(BaseModel):
    role: str
    content: Union[str, List[ChatCompletionContentPartParam]]


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    image: Optional[str] = Field(default=None)
    max_tokens: Optional[int] = Field(default=100)
    stream: Optional[bool] = Field(default=False)
    temperature: Optional[float] = Field(default=0.2)
    tools: Optional[List[Function]] = Field(default=None)
    tool_choice: Optional[str] = Field(default=None)
    stream_options: Optional[Dict[str, Any]] = Field(default=None)


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    usage: Usage
    choices: List[dict]
    tool_calls: Optional[List[ToolCall]] = None


class ChatCompletionChunk(BaseModel):
    id: str
    object: str = "chat.completion.chunk"
    created: int
    model: str
    choices: List[Dict[str, Any]]
    usage: Optional[Usage] = None
