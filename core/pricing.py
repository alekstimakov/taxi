from abc import ABC, abstractmethod
from core.models import Order

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, order:Order) -> float:
        """Расчитывает стоимость заказа"""

class FlatRateStrategy(PricingStrategy):
    """Фиксированная стоимость поездки"""
    def calculate(self, order:Order) -> float:
        return 200.0

class DistanceBasedStrategy(PricingStrategy):
    """Расчитывает стоимость поездки в зависимости от расстояния"""
    def calculate(self, order:Order) -> float:
        basic_tariff = 200
        return order.dictance * 100 + basic_tariff