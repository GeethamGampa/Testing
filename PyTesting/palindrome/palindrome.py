# 13. palindrome.py

def check_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]
