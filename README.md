# age-calculator
- A Python application that calculates a person's exact age in years, months, and days using the datetime module. -
# Age Calculator

A simple command-line application that calculates your exact age in **years, months, and days** from your date of birth.

Built with Python's standard `datetime` and `calendar` modules, so no external libraries are needed.

## Features

- Calculates exact age in years, months, and days
- Handles leap years and months of different lengths (28, 29, 30, 31 days)
- Handles edge cases such as births on the 29th, 30th, or 31st
- Validates user input:
  - Wrong format (e.g. `abc`)
  - Impossible calendar dates (e.g. `30/02/2000`)
  - Future dates
  - Unrealistic years (before 1900)
- Interactive CLI that keeps asking until you type `q` to quit

## Requirements

- Python 3.7 or later
- No third-party packages

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/age-calculator.git
   cd age-calculator
   ```

2. Run the program:

   ```bash
   python age_calculator.py
   ```

3. Enter your birth date in `DD/MM/YYYY` format. Type `q` to quit.

## Example Session

```
=== Age Calculator ===
Type 'q' to quit.

Enter your birth date (DD/MM/YYYY): 15/03/2000
Your age is: 26 years , 8 months , 6 days

Enter your birth date (DD/MM/YYYY): 30/02/2000
Error: Invalid date. Use DD/MM/YYYY and a real calendar date.

Enter your birth date (DD/MM/YYYY): 01/01/2030
Error: Birth date cannot be in the future.

Enter your birth date (DD/MM/YYYY): q
Goodbye!
```

## How It Works

The project has three main functions:

| Function | Purpose |
| --- | --- |
| `calculate_age(birth, today=None)` | Returns `(years, months, days)` between two dates |
| `parse_birth_date(text, today=None)` | Converts `DD/MM/YYYY` text to a date and validates it |
| `main()` | Runs the interactive loop |

### Age calculation logic

1. Count the total number of complete months between the birth date and today. If today's day is smaller than the birth day, the current month is not complete yet, so one month is subtracted.
2. Split the total months into years and remaining months with `divmod(total_months, 12)`.
3. Find the last "monthly anniversary" (the anchor date). Days are counted from that date to today. If the birth day does not exist in that month (for example the 31st in a 30-day month), the last day of the month is used instead.

This avoids the common mistake of dividing days by 365, which is wrong for leap years.

## Tested Cases

| Birth date | Today | Result |
| --- | --- | --- |
| 15/03/2000 | 21/11/2026 | 26 years, 8 months, 6 days |
| 31/01/2024 | 01/03/2024 | 0 years, 1 month, 1 day |
| 30/02/2000 | any | Error: invalid date |
| 01/01/2030 | 2026 | Error: future date |

## Project Structure

```
age-calculator/
├── age_calculator.py
└── README.md
```

## Author

Shimaa Mostafa

Created as part of the Pynexia Python Programming internship.
