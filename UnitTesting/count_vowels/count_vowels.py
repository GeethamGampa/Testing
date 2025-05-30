# 4. Count Vowels

def count_vowels_in_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
