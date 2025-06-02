# 6. factorial.py

def factorial_calc(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
