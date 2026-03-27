import requests
from core.models import Point, OSRMResponse
from utils.folium_map import get_folium_map
host = "http://router.project-osrm.org/"
service = "route"
version = "v1"
profile = "driving"

# координаты: Долгота, широта
kazan_cathedral = Point(longitude=30.32388, latitude=59.934214)
winter_palace = Point(longitude=30.313621, latitude=59.939763)
center_point = Point(longitude=30.318301, latitude=59.938333)

coordinates = (
    f"{kazan_cathedral.longitude},{kazan_cathedral.latitude};"
    f"{winter_palace.longitude},{winter_palace.latitude}"
)


url = f"{host}/{service}/{version}/{profile}/{coordinates}?overview=full&geometries=geojson"

responce = requests.get(url)

data = OSRMResponse.model_validate(responce.json())
route = data.routes[0]


folium_map = get_folium_map(
    center=center_point,
    markers=[kazan_cathedral,winter_palace],
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
