import requests

from core.models import OSRMResponse, Point
from utils.folium_map import get_folium_map

host = "https://router.project-osrm.org"
service = "route"
version = "v1"
profile = "driving"

# координаты: Долгота, широта
start_point = Point(longitude=30.304768, latitude=59.980180)
end_point = Point(longitude=30.296093, latitude=59.925619)
center_point = Point(longitude=30.318301, latitude=59.938333)

coordinates = (
    f"{start_point.longitude},{start_point.latitude};"
    f"{end_point.longitude},{end_point.latitude}"
)


url = f"{host}/{service}/{version}/{profile}/{coordinates}?overview=full&geometries=geojson"
headers = {"Referer": "http://127.0.0.1:8000/"}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    payload = response.json()
except requests.RequestException as exc:
    raise SystemExit(f"Ошибка запроса к OSRM: {exc}") from exc
except ValueError as exc:
    raise SystemExit(f"Некорректный JSON от OSRM: {exc}") from exc

data = OSRMResponse.model_validate(payload)
route = data.routes[0]


folium_map = get_folium_map(
    center=center_point,
    markers=[start_point, end_point],
    path=route.geometry.coordinates,
    distance=route.distance,
    duration=route.duration
)


output_file = "route_map.html"
folium_map.save(output_file)
# print(data.routes[0].geometry.coordinates)
# print(f'Статус ответа: {responce.status_code}')
# # print('Ответ от сервера:')
# # print(responce.text)
