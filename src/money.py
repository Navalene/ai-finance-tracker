def format_amount(cents: int) -> str:
    """Turn integer cents into a dollar string.

    Examples:
        1234  -> "12.34"
        5     -> "0.05"
        -150  -> "-1.50"
    """
    # Step 1: remember if the number is negative, then work with the positive version.
    sign = "-" if cents < 0 else ""
    positive_cents = abs(cents)

    # Step 2: split into whole dollars and leftover cents.
    dollars, leftover_cents = divmod(positive_cents, 100)

    # Step 3: glue it together. :02d means "always show 2 digits" (5 -> "05").
    return f"{sign}{dollars}.{leftover_cents:02d}"


def parse_amount(text: str) -> int:
    """Turn a dollar string into integer cents.

    Examples:
        "12.34"     -> 1234
        "12"        -> 1200
        "12.5"      -> 1250
        "-1.50"     -> -150
        "$1,234.56" -> 123456
    Anything that isn't a valid amount raises ValueError.
    """
    # Step 1: clean up. Remove spaces at the ends, dollar signs, and commas.
    cleaned = text.strip().replace("$", "").replace(",", "")

    # Step 2: remember the minus sign, then remove it.
    sign = 1
    if cleaned.startswith("-"):
        sign = -1
        cleaned = cleaned[1:]

    # Step 3: split at the dot into a dollars part and a cents part.
    if "." in cleaned:
        dollars_part, cents_part = cleaned.split(".", 1)
    else:
        dollars_part, cents_part = cleaned, ""

    # Step 4: check that what's left is really a money amount.
    if dollars_part == "" and cents_part == "":
        raise ValueError(f"Not a valid amount: {text!r}")
    if dollars_part == "":
        dollars_part = "0"  # ".50" means "0.50"
    if not dollars_part.isdigit():
        raise ValueError(f"Not a valid amount: {text!r}")
    if cents_part != "" and not cents_part.isdigit():
        raise ValueError(f"Not a valid amount: {text!r}")
    if len(cents_part) > 2:
        raise ValueError(f"Too many digits after the dot: {text!r}")

    # Step 5: make cents exactly 2 digits ("5" -> "50", "" -> "00"), then add it up.
    cents_part = cents_part.ljust(2, "0")
    return sign * (int(dollars_part) * 100 + int(cents_part))