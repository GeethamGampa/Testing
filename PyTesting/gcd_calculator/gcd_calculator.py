# 8. gcd_calculator.py

def gcd(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    while b:
        a, b = b, a % b
    return abs(a)
