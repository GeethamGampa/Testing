# 18. square.py

def square_num(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number")
    return num * num
