ROMAN_MAP = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


def roman(number):
    output = ''
    for index, (arabic, roman) in enumerate(ROMAN_MAP.items()):
        while number >= arabic:
            number -= arabic
            output += roman
    return output
