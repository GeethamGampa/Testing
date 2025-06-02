# 12. max_of_two.py

def max_num(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Inputs must be numbers")
    return a if a > b else b
