# 18. Square of a Number

def square_num(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    return n ** 2
