import folium
from branca.element import Element

from core.models import Point


def get_folium_map(
        center: Point,
        markers: list[Point],
        path: list[list[float]],
        distance: float,
        duration: float,
        zoom_level: int = 15) \
    -> folium.Map:
    """Создает интерактивную карту с заданными точками.

    Args:
        center(Point) : Точка относительно которой будет центр карты
        markers(list[Point]): Список точек для отображения
        zoom_level (int): Уровень приближения.
        path: list[list[float]]: Путь из точек
        distance: float, Дистанция
        duration: float, Длительность
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

    popup_html = (
        f'<b>Расстояние:</b> {distance:.1f} m<br>'
        f'<b>Время:</b> {duration:.1f} сек (~{duration/60:.1f} мин)'
    )
    popup = folium.Popup(popup_html, max_width=300)
    route_points = [[lat, lon] for lon, lat in path]


    line = folium.PolyLine(
        locations=route_points,
        color="blue",
        weight=5,
        popup=popup
    ).add_to(map)
    if route_points:
        map.fit_bounds(route_points)
    return map
