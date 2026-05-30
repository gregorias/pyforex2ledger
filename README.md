# pyforex2ledger

This tool prints currency exchange rates in [plain text account
format](https://plaintextaccounting.org/), e.g.;

```bash
$ forex2ledger --config_file config-sample.toml
P 2021-03-21 USD 0.929777 CHF
P 2021-03-21 USD 0.836925 EUR
```

## Installation

You can install `pyforex2ledger` using `uv`:

```bash
uv tool install .
```

Alternatively, you can install it using `pipx`:

```bash
pipx install .
```

## Usage

You will need a valid app ID from
[Open Exchange Rates](http://openexchangerates.org).

1. Add a valid app ID to your config file.
2. Run `forex2ledger --config_file your_config.toml`.

By default, the tool will look for a configuration file at `$XDG_CONFIG_HOME/findata/forex2ledger.toml`.

### Sample config file

An example config file looks like this:

```toml
# config-sample.toml
# The AppId for https://openexchangerates.org/
oer_app_id = 'SAMPLEAPPID'
currency.base = 'USD'
currency.targets = ['CHF', 'EUR']
```
