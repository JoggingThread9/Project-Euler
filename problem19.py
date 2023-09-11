def leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

day = 1
year = 1900
month = 1
date = 1

sundays = 0

extra_days = [1,3,5,7,8,10,12]

while year < 2001:
    if day == 7 and date == 1 and year > 1900:
        sundays += 1

    # day
    if day == 7:
        day = 1
    else:
        day += 1

    # year
    if date == 31 and month == 12:
        year += 1

    # month
    if month == 2:
        days_in_month = 29 if leap(year) else 28
    else:
        days_in_month = 31 if month in extra_days else 30

    if date == days_in_month:
        if month == 12:
            month = 1
        else:
            month += 1
        date = 1
    else:
        date += 1

print(sundays)