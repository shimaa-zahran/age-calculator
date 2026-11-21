import calendar
import datetime as dt


def calculate_age(birth, today=None):
    """Return (years, months, days) between the birth date and today."""
    today = today or dt.date.today()

    # 1) Count the total number of complete months
    total_months = (today.year - birth.year) * 12 + (today.month - birth.month)
    if today.day < birth.day:
        total_months -= 1  # the current month is not complete yet

    years, months = divmod(total_months, 12)

    # 2) Find the last "monthly anniversary" (anchor) and count days from it
    index = birth.month - 1 + total_months
    anchor_year = birth.year + index // 12
    anchor_month = index % 12 + 1
    last_day = calendar.monthrange(anchor_year, anchor_month)[1]
    # min() handles births on the 29th/30th/31st in shorter months
    anchor = dt.date(anchor_year, anchor_month, min(birth.day, last_day))

    days = (today - anchor).days
    return years, months, days


def parse_birth_date(text, today=None):
    """Convert 'DD/MM/YYYY' text to a date. Raise ValueError with a clear message."""
    today = today or dt.date.today()

    try:
        birth = dt.datetime.strptime(text.strip(), "%d/%m/%Y").date()
    except ValueError:
        # Covers wrong format AND impossible dates like 30/02/2000
        raise ValueError("Invalid date. Use DD/MM/YYYY and a real calendar date.")

    if birth > today:
        raise ValueError("Birth date cannot be in the future.")

    if birth.year < 1900:
        raise ValueError("Birth year must be 1900 or later.")

    return birth


def plural(number, word):
    """Return '1 year' / '2 years' style text."""
    return f"{number} {word}" + ("" if number == 1 else "s")


def main():
    print("=== Age Calculator ===")
    print("Type 'q' to quit.")

    while True:
        text = input("\nEnter your birth date (DD/MM/YYYY): ")

        if text.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        try:
            birth = parse_birth_date(text)
        except ValueError as error:
            print("Error:", error)
            continue  # ask again

        years, months, days = calculate_age(birth)
        print(
            "Your age is:",
            plural(years, "year"), ",",
            plural(months, "month"), ",",
            plural(days, "day"),
        )


if __name__ == "__main__":
    main()