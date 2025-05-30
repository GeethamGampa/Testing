# 11. Leap Year Checking

def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 0:
        raise ValueError("Year must be positive")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
