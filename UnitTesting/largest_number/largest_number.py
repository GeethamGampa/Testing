# 10. Finding Largest Number

def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("List cannot be empty")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("List elements must be numbers")
    return max(numbers)
