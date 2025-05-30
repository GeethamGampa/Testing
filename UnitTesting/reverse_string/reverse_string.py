# 16. Reversing a String

def reverse_str(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]
