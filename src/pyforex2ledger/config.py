from dataclasses import dataclass
from typing import Any


@dataclass
class Config:
    oer_app_id: str
    base_currency: str
    target_currencies: list[str]


def parse_config(data: dict[str, Any]) -> Config:
    oer_app_id = data["oer_app_id"]
    base_currency = data["currency"]["base"]
    target_currencies = data["currency"]["targets"]
    return Config(
        oer_app_id=oer_app_id,
        base_currency=base_currency,
        target_currencies=target_currencies,
    )
