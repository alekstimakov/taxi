import requests

host = "http://router.project-osrm.org/"
service = "route"
version = "v1"
profile = "driving"

# координаты: Долгота, широта
kazan_cathedral = "30.323885,59.934214"
winter_palace = "30.313621,59.939763"

coordinates = f"{kazan_cathedral};{winter_palace}"


url = f"{host}/{service}/{version}/{profile}/{coordinates}?overview=full&geometries=geojson"

responce = requests.get(url)

print(f'Статус ответа: {responce.status_code}')
print('Ответ от сервера:')
print(responce.text)
