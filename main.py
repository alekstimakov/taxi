import requests
from core.models import Point
host = "https://router.project-osrm.org/"
service = "route"
version = "v1"
profile = "driving"

# координаты: Долгота, широта
kazan_cathedral = Point(longitude=30.32388, latitude=59.934214)
winter_palace = Point(longitude=30.313621, latitude=59.939763)

coordinates = f"{kazan_cathedral.latitude},{kazan_cathedral.latitude};{winter_palace.latitude},{winter_palace.longitude}"


url = f"{host}/{service}/{version}/{profile}/{coordinates}?overview=full&geometries=geojson"

responce = requests.get(url)

print(f'Статус ответа: {responce.status_code}')
print('Ответ от сервера:')
print(responce.text)
