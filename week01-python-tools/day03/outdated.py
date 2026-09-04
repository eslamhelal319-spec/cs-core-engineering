# The problem :
# the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
# otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted
# because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900,
# and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous.
# Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!
# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
# no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.
# implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
# wherein the month in the latter might be any of the values in the list 
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
# prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
 

# The solution :

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month, day, year = date.split(" ")

            if not day.endswith(","):
                raise ValueError

            month = months.index(month) + 1
            day = int(day.replace(",", ""))
            year = int(year)

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

    except (ValueError, IndexError):
        continue

    else:
        print(f"{year:04}-{month:02}-{day:02}")
        break
