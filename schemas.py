from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class CreateAdRequest(BaseModel):
    title: str
    description: str
    price: float = Field(gt=0)
    author: str

class UpdateAdRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    author: str | None = None

class AdResponse(BaseModel):
    id: int 
    title: str
    description: str
    price: float
    author: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


