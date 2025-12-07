#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    if roman_string == "":
        return 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    prev_value = 0
    for ch in reversed(roman_string):
        if ch not in roman:
            return 0
        value = roman[ch]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total
