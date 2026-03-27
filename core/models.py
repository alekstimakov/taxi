import math
from typing import Any

from pydantic import BaseModel, Field


class Point(BaseModel):
    longitude: float = Field(..., description="Долгота точки")
    latitude: float = Field(..., description="Широта точки")

    def __sub__(self, b_point: Point) -> float:
        earth_radius = 6371.0

         # Переводим градусы в радианы
        phi1 = math.radians(self.latitude)
        phi2 = math.radians(b_point.latitude)
        dph1 = math.radians(b_point.longitude- self.latitude)
        dlambda = math.radians(b_point.longitude - self.longitude)

        a = math.sin(dph1 / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return earth_radius * c


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


class Order(BaseModel):
    point_a: Point = Field(..., description="Начальная точка маршрута")
    point_b: Point = Field(..., description="Конечная точка маршрута")

    @property
    def distance(self) -> float:
        """Вычисляет расстояние между двумя точками в километрах"""
        return self.point_a - self.point_b