import folium
from branca.element import Element

from core.models import Point


def get_folium_map(center: Point, markers:list[Point], zoom_level: int = 15) -> folium.Map:
    """Создает интерактивную карту с заданными точками.

    Args:
        center(Point) : Точка относительно которой будет центр карты
        markers(list[Point]): Список точек для отображения
        zoom_level (int): Уровень приближения.
    """
    map = folium.Map(location=[center.latitude,center.longitude],zoom_start=zoom_level)
    map.get_root().header.add_child(
        Element('<meta name="referrer" content="strict-origin-when-cross-origin">')
    )

    for idx, pt in enumerate(markers):
        label = "Начало поездки" if idx == 0 else "Конец поездки"
        color = "green" if idx == 0 else "red"
        folium.Marker(
            [pt.latitude, pt.longitude],
            popup=label,
            icon=folium.Icon(color=color),
        ).add_to(map)
    return map
