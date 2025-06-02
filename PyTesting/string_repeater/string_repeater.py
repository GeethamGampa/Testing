# 19. string_repeater.py

def repeater(s, times):
    if not isinstance(s, str):
        raise TypeError("First argument must be a string")
    if not isinstance(times, int):
        raise TypeError("Second argument must be an integer")
    if times < 0:
        raise ValueError("Times must be non-negative")
    return s * times
