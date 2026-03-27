from typing import Any

from pydantic import BaseModel, Field


class Point(BaseModel):
    longitude: float = Field(..., description="Долгота точки")
    latitude: float = Field(..., description="Широта точки")


class Geometry(BaseModel):
    type: str = Field(..., description="Тип геометрии, например LineString")
    coordinates: list[list[float]] = Field(
        ..., description="Список координат маршрута (долгота, широта)"
    )


class Leg(BaseModel):
    steps: list[Any] = Field(default_factory=list, description="Шаги маршрута")
    weight: float = Field(..., description="Внутренний вес маршрута")
    summary: str = Field(..., description="Краткое описание участка маршрута")
    duration: float = Field(..., description="Длительность участка в секундах")
    distance: float = Field(..., description="Дистанция участка в метрах")


class Route(BaseModel):
    legs: list[Leg]
    weight_name: str
    geometry: Geometry
    duration: float
    distance: float


class Waypoint(BaseModel):
    hint: str
    location: list[float]
    name: str
    distance: float


class OSRMResponse(BaseModel):
    code: str
    routes: list[Route]
    waypoints: list[Waypoint]
