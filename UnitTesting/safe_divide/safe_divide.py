# 17. safe_divide 

def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
