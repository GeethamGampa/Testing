# 5. count_words.py

def count_words_in_sentence(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = text.split()
    return len(words)
