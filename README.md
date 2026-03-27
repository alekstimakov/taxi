# Taxi Route Map

Небольшой учебный проект на Python:
- запрашивает маршрут между двумя точками через OSRM;
- строит интерактивную карту через Folium;
- сохраняет результат в `route_map.html`;
- считает стоимость поездки через стратегии ценообразования.

## Требования

- Python 3.14+ (или близкая версия 3.x)
- виртуальное окружение `venv`

## Установка зависимостей

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Построение маршрута и карты

```powershell
venv\Scripts\python.exe main.py
```

После запуска появится файл `route_map.html`.

## Корректное открытие карты

Для OpenStreetMap лучше открывать карту через HTTP, а не как `file://`.

```powershell
venv\Scripts\python.exe serve_map.py
```

Далее открыть в браузере:
`http://127.0.0.1:8000/route_map.html`

## Проверка ценообразования

Файл `core/pricing_check.py` создаёт тестовый заказ и выводит стоимость.

Запуск со стратегией по умолчанию:

```powershell
python -m core.pricing_check
```

Запуск с фиксированной ценой:

```powershell
$env:PRICING_STRATEGY_NAME="flat_rate"; python -m core.pricing_check
```

Запуск с "первоапрельской" стратегией:

```powershell
$env:PRICING_STRATEGY_NAME="first_aprel"; python -m core.pricing_check
```

## Доступные стратегии

- `default` - расстояние по формуле Хаверсина и тариф `200 + distance * 100`
- `flat_rate` - фиксированная цена `200`
- `first_aprel` - случайная цена от `100` до `200000`

## Структура проекта

- `main.py` - запрос маршрута и генерация карты
- `core/models.py` - Pydantic-модели и расчёт расстояния между точками
- `core/pricing.py` - стратегии расчёта стоимости поездки
- `core/pricing_check.py` - проверка стратегий ценообразования
- `utils/folium_map.py` - отрисовка карты, маркеров и линии маршрута
