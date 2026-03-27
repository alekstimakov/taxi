from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pricing_strategy_name: str = Field(
        default="default",
        description="Стратегия расчёта цены заказа.",
    )
