# 14. Power Calculator

def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent
