def rotate(text, key):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    translator = ALPHABET[key:] + ALPHABET[:key]

    transtab = str.maketrans(ALPHABET + ALPHABET.upper(), translator +
                             translator.upper())

    return text.translate(transtab)

# below is my initial solution.
# decided to rewrite my solution to try the translation function
#
# ALPA_NUM = 26
#
#
# def rotate_char(code, code_a, key):
#     return chr((code - code_a + key) % ALPA_NUM + code_a)
#
#
# def rotate(text, key):
#     result = ''
#     char_a = ord('a')
#     char_A = ord('A')
#     for char in [*text]:
#         if char.isalpha():
#             ascii_code = ord(char)
#             if char.isupper():
#                 result += rotate_char(ascii_code, char_A, key)
#             else:
#                 result += rotate_char(ascii_code, char_a, key)
#         else:
#             result += char
#
#     return result
