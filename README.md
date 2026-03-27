# Taxi Route Map

Небольшой учебный проект на Python:
- запрашивает маршрут между двумя точками через OSRM;
- строит интерактивную карту через Folium;
- сохраняет результат в `route_map.html`.

## Что нужно

- Python 3.14+ (или близкая версия 3.x)
- Виртуальное окружение `venv`

## Установка зависимостей

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Построить маршрут и карту

```powershell
venv\Scripts\python.exe main.py
```

После запуска появится файл `route_map.html`.

## Открыть карту корректно (без блокировки тайлов)

Для OpenStreetMap карту лучше открывать через HTTP, а не как `file://`.

```powershell
venv\Scripts\python.exe serve_map.py
```

Потом открыть в браузере:

`http://127.0.0.1:8000/route_map.html`

## Структура проекта

- `main.py` — запрос маршрута и генерация карты
- `core/models.py` — Pydantic-модели ответа OSRM
- `utils/folium_map.py` — отрисовка карты, маркеров и линии маршрута
- `serve_map.py` — локальный HTTP-сервер для корректной загрузки тайлов
