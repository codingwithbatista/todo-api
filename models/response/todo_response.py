from typing import Optional
from pydantic import BaseModel, Field


class TodoResponse(BaseModel):
    id : Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(ge=1, le=5)
    complete: bool = Field(default=False)
