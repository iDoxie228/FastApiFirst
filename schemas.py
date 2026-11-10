from pydantic import BaseModel, ConfigDict
from datetime import date


class CreateAdRequest(BaseModel):
    title: str
    description: str
    price: float
    author: str

class UpdateAdRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    author: str | None = None

class AdResponse(BaseModel):
    id: int 
    title: str
    description: str
    price: float
    author: str
    created_at: date

    model_config = ConfigDict(from_attributes=True)


