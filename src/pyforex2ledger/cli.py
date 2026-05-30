import argparse
import os
import sys
import tomllib

from .config import parse_config
from .oer import fetch_rates
from .ledger import rates_to_ledger


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="forex2ledger", description="Print Forex rates in Ledger format."
    )

    default_config = None
    config_home = os.environ.get("XDG_CONFIG_HOME")
    if config_home:
        default_config = os.path.join(config_home, "findata", "forex2ledger.toml")

    parser.add_argument(
        "--config_file",
        metavar="FILE",
        help="The TOML config file.",
        default=default_config,
    )

    args = parser.parse_args()

    if not args.config_file:
        print(
            "Config file path is required if XDG_CONFIG_HOME is not set.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        with open(args.config_file, "rb") as f:
            config_data = tomllib.load(f)
    except Exception as e:
        print("Could not parse the config file.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)

    try:
        config = parse_config(config_data)
    except Exception as e:
        print("Invalid config file format.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)

    try:
        rates = fetch_rates(config)
    except Exception as e:
        print("Could not fetch rates from OER.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)

    print(rates_to_ledger(config.base_currency, rates), end="")


if __name__ == "__main__":
    main()
