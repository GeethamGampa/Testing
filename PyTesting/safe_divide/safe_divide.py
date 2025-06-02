# 17. safe_divide.py

def safe_division(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
