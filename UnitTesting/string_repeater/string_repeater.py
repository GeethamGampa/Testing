# 19. String Repeater

def repeat_string(s, n):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(n, int):
        raise TypeError("Repeat count must be an integer")
    if n < 0:
        raise ValueError("Repeat count must be non-negative")
    return s * n
