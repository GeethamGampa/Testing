# 11. leap_year_checker.py

def leap_check(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 0:
        raise ValueError("Year must be a positive integer")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
