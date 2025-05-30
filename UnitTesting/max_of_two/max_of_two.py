# 12. Max of Two Numbers

def max_of_two_num(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")
    return a if a > b else b
