from .oer import OerRates


def show_market_price(day: str, base: str, target: str, price: float) -> str:
    return f"P {day} {base} {price} {target}\n"


def rates_to_ledger(base: str, oer_rates: OerRates) -> str:
    day_str = oer_rates.timestamp.strftime("%Y-%m-%d")
    result = []
    for target, price in oer_rates.rates.items():
        result.append(show_market_price(day_str, base, target, price))
    return "".join(result)
