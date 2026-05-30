import unittest
from datetime import datetime, timezone
from pyforex2ledger.oer import OerRates
from pyforex2ledger.ledger import rates_to_ledger, show_market_price


class TestLedger(unittest.TestCase):
    def test_show_market_price(self):
        self.assertEqual(show_market_price("2024-05-18", "EUR", "USD", 1.08), "P 2024-05-18 EUR 1.08 USD\n")

    def test_rates_to_ledger(self):
        timestamp = datetime(2024, 5, 18, 12, 0, 0, tzinfo=timezone.utc)
        rates = OerRates(timestamp=timestamp, rates={"USD": 1.08, "CHF": 0.98})
        result = rates_to_ledger("EUR", rates)
        expected = "P 2024-05-18 EUR 1.08 USD\nP 2024-05-18 EUR 0.98 CHF\n"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
