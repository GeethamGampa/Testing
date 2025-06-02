# 16. reverse_string.py

def rev_str(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]
