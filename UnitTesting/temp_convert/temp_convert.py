# 20. Temperature Conversion

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    return (celsius * 9/5) + 32
