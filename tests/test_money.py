import pytest

from src.money import format_amount, parse_amount


# ---------- format_amount: cents -> text ----------

def test_whole_dollars():
    assert format_amount(1200) == "12.00"


def test_cents():
    assert format_amount(99) == "0.99"


def test_zero():
    assert format_amount(0) == "0.00"


def test_five_cents():
    assert format_amount(5) == "0.05"


def test_dollars_and_cents():
    assert format_amount(1234) == "12.34"


def test_negative_amount():
    # A refund or money going out: -150 cents is -$1.50, not -$2.50
    assert format_amount(-150) == "-1.50"


def test_small_negative():
    assert format_amount(-5) == "-0.05"


def test_big_amount():
    assert format_amount(123456789) == "1234567.89"


# ---------- parse_amount: text -> cents ----------

def test_parse_dollars_and_cents():
    assert parse_amount("12.34") == 1234


def test_parse_whole_dollars():
    assert parse_amount("12") == 1200


def test_parse_one_decimal_digit():
    # "12.5" means 12 dollars and 50 cents, not 5 cents
    assert parse_amount("12.5") == 1250


def test_parse_negative():
    assert parse_amount("-1.50") == -150


def test_parse_dollar_sign_and_comma():
    assert parse_amount("$1,234.56") == 123456


def test_parse_spaces_around():
    assert parse_amount("  7.00 ") == 700


def test_parse_no_leading_zero():
    assert parse_amount(".50") == 50


def test_round_trip():
    # parse should undo format: cents -> text -> the same cents
    for cents in [0, 5, 99, 1234, -150, 123456789]:
        assert parse_amount(format_amount(cents)) == cents


# ---------- parse_amount: bad input should raise ValueError ----------

def test_parse_rejects_words():
    with pytest.raises(ValueError):
        parse_amount("abc")


def test_parse_rejects_empty():
    with pytest.raises(ValueError):
        parse_amount("")


def test_parse_rejects_three_decimals():
    with pytest.raises(ValueError):
        parse_amount("1.234")


def test_parse_rejects_two_dots():
    with pytest.raises(ValueError):
        parse_amount("1.2.3")