import random
from abc import ABC, abstractmethod

from core.models import Order


class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, order: Order) -> float:
        """Рассчитывает стоимость заказа."""


class FlatRateStrategy(PricingStrategy):
    """Фиксированная стоимость поездки."""

    def calculate(self, order: Order) -> float:
        return 200.0


class DistanceBasedStrategy(PricingStrategy):
    """Стоимость зависит от расстояния."""

    def calculate(self, order: Order) -> float:
        basic_tariff = 200
        return order.distance * 100 + basic_tariff


class FirstAprelPrice(PricingStrategy):
    """Первоапрельская стратегия: случайная цена в большом диапазоне."""

    def calculate(self, order: Order) -> float:
        return float(random.randint(100, 200000))
