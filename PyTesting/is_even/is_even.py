# 9. is_even.py

def is_even_num(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    return num % 2 == 0
