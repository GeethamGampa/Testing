# 14. power_calculator.py

def power(base, exponent):
    if not all(isinstance(x, (int, float)) for x in [base, exponent]):
        raise TypeError("Inputs must be numbers")
    return base ** exponent
