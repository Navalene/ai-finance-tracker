# AI Finance Tracker

A personal finance tracker I'm building from scratch in Python as part of my Computer Science studies at SNHU. The goal is an app that stores transactions in SQLite and uses AI to sort them into spending categories automatically.

> **Status: in progress (early stage).** The money-handling core is built and tested. Storage, the command-line interface, and AI categorization are next.

## What works now

- **Money is stored as whole cents, not decimals.** Decimal numbers (floats) can't store some amounts exactly. For example, `0.1 + 0.2` gives `0.30000000000000004` in Python, which causes rounding errors in financial math. Using integer cents avoids that.
- `parse_amount()` turns text a user types into an amount in cents.
- `format_amount()` turns cents back into a readable dollar amount.
- **20 unit tests** with pytest cover both functions.

## Roadmap

- [x] Money parsing and formatting, with tests
- [ ] Transaction data model
- [ ] Save transactions in a SQLite database
- [ ] Command-line interface: add transactions, list them, and see totals by category
- [ ] AI auto-categorization using the Anthropic API
- [ ] Labeled test set to measure how accurate the AI categories are
- [ ] Cost tracking for each API call, plus a rule-based fallback when the API isn't available

## Tech stack

- Python 3.9+
- pytest
- SQLite (planned, built into Python)
- Anthropic API (planned)

## Project structure

```
src/
  money.py      # parse and format money amounts (done)
  models.py     # transaction data model (planned)
  db.py         # SQLite storage (planned)
  cli.py        # command-line interface (planned)
tests/
  test_money.py # tests for money.py
```

## Run the tests

```bash
git clone https://github.com/navalene/ai-finance-tracker.git
cd ai-finance-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest
```

## About me

I'm Jaylene Navarrete, a Computer Science student moving into data and AI engineering.
[LinkedIn](https://www.linkedin.com/in/jaylene-navarrete)