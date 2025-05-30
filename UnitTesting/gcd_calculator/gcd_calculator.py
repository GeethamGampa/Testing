# 8. Calculating GCD

def gcd(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    while b:
        a, b = b, a % b
    return abs(a)
