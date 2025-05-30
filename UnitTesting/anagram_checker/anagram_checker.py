# 2. Anagram Checker

def are_anagrams(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Inputs must be strings")
    
    # Remove spaces and convert to lowercase
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    # Checking if the sorted characters are the same
    return sorted(s1_clean) == sorted(s2_clean)
