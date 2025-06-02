# 2. anagram_checker.py

def are_anagrams(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
