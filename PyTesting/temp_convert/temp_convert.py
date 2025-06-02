# 20. temp_convert.py

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number")
    return (fahrenheit - 32) * 5/9
