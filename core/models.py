from pydantic import BaseModel,Field
from typing import Any


class Point(BaseModel):
    """Модель точки на карте."""
    longitude: float = Field(..., description="Долгота точки")
    latitude: float = Field(..., description="Широта точки")


class Geometry(BaseModel):
    """Геометрия маршрута"""
    type:str = Field(...,description="Тип геометрии. Например 'LineString")
    list[list[float]] = Field(...,description="Список координат маршрута (Долгота,Широта)")


class Leg(BaseModel):
    """Этап маршрута между двумя точками"""
    steps: list[Any] = Field(default_factory=list, description="ds")
    weight: float = Field(...,description="Внутренняя стоимость")
    summary: str = Field(...,description="Краткое описание участка маршрута")
    duration: float = Field(...,description="Длительность в секундах участка маршрута")
    distance: float = Field(...,description="Полная дистанция маршрута")


class Route(BaseModel):
    """Основной маршрут"""
    legs: list[Leg]
    weight_name: float
    geometry: Geometry
    duration: float
    distance: float


class Waypoint(BaseModel):
    """Ключевая точка маршрута"""
    hints: str
    location: tuple[float,float]
    name: str
    distance: float

class OSRMResponse(BaseModel):
    """Корневая модель ответа от OSRM"""
    code: str
    routes: list[Route]
    waypoints: list[Waypoint]