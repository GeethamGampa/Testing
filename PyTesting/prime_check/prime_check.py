# 15. prime_check.py

def check_prime(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
