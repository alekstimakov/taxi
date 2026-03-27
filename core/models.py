from pydantic import BaseModel,Field


class Point(BaseModel):
    longitude: float = Field(..., description="Долгота точки")
    latitude: float = Field(..., description="Широта точки")

