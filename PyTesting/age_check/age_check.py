# 1. age_check.py

def is_adult(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    return age >= 18
