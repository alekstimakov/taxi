from typing import Type

from core.config import Settings
from core.models import Order, Point
from .pricing import DistanceBasedStrategy, FlatRateStrategy, PricingStrategy, FirstAprelPrice

strategy_map: dict[str, Type[PricingStrategy]] = {
    "default": DistanceBasedStrategy,
    "flat_rate": FlatRateStrategy,
    "first_aprel": FirstAprelPrice,
}


if __name__ == "__main__":
    point_a = Point(longitude=30.323471, latitude=59.934525)
    point_b = Point(longitude=30.32355, latitude=59.93428)
    order = Order(point_a=point_a, point_b=point_b)

    settings = Settings()
    # Выбор стратегии через переменную окружения PRICING_STRATEGY_NAME.
    pricing_strategy = strategy_map[settings.pricing_strategy_name]()
    price = pricing_strategy.calculate(order)
    print(price)
