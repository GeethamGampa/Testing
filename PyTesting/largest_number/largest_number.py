# 10. largest_number.py

def find_largest(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("All inputs must be numbers")
    return max(a, b, c)
