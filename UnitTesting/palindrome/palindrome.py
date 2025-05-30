# 13. Palindrome

def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    text = s.replace(" ", "").lower()
    return text == text[::-1]
