import json
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone

from .config import Config


@dataclass
class OerRates:
    timestamp: datetime
    rates: dict[str, float]


def fetch_rates(config: Config) -> OerRates:
    base_url = "https://openexchangerates.org/api/latest.json"
    params = {
        "app_id": config.oer_app_id,
        "base": config.base_currency,
        "symbols": ",".join(config.target_currencies),
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            raise RuntimeError(f"Received a non-200 response code: {response.status}")
        data = json.loads(response.read().decode("utf-8"))

    timestamp = datetime.fromtimestamp(data["timestamp"], tz=timezone.utc)
    rates = data["rates"]
    return OerRates(timestamp=timestamp, rates=rates)
