# 5. Count Words

def count_words_in_sentence(sentence):
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    words = sentence.split()
    return len(words)
