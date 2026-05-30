import unittest
from pyforex2ledger.config import parse_config


class TestConfig(unittest.TestCase):
    def test_parse_config(self):
        data = {
            "oer_app_id": "secret123",
            "currency": {
                "base": "EUR",
                "targets": ["USD", "CHF"]
            }
        }
        config = parse_config(data)
        self.assertEqual(config.oer_app_id, "secret123")
        self.assertEqual(config.base_currency, "EUR")
        self.assertEqual(config.target_currencies, ["USD", "CHF"])


if __name__ == "__main__":
    unittest.main()
