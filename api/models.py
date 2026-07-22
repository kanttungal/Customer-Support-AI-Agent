from typing import Optional, List
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    query: str = Field(..., description="Customer query")
    session_id: Optional[str] = Field(
        default=None,
        description="Unique session ID for the conversation"
    )


class Source(BaseModel):
    source: str
    page: Optional[int] = None


class ChatResponse(BaseModel):
    answer: str
    category: str
    sources: List[Source] = []
    session_id: Optional[str] = None