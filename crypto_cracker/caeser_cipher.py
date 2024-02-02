import string
from util import get_dictionary, detect_english

LETTERS = string.ascii_uppercase

"""
util function to convert char key to int
"""


def convert_to_int(key) -> int:
    if type(key) == str:
        # assume it's a one letter code for offset
        int_key = key[0].upper()
        try:
            key = string.ascii_uppercase.index(int_key)
        except:
            raise TypeError("Key is not a int or a single character")

    if type(key) != int:
        raise TypeError("Key is not a int or a single character")

    return key


def encrypt(plain_text: str, key: int) -> str:
    # convert everything to uppercase
    plain_text = plain_text.upper()
    result_text = ''
    for char in plain_text:
        if char in LETTERS:
            result_text += LETTERS[(LETTERS.index(char) + key) % 26]
        else:
            result_text += char

    return result_text


def decrypt(cipher_text: str, key) -> str:
    return encrypt(cipher_text, -key)


def test():
    # unit test
    # print(encrypt('Welcome to ninety-eighty-four!', convert_to_int('x')))
    for char in string.ascii_uppercase:
        # print(char, ': ', decrypt(
        #     "TBIZLJB QL KFKBQV-BFDEQV-CLRO!", convert_to_int(char)))
        if detect_english(decrypt("TBIZLJB QL KFKBQV-BFDEQV-CLRO!", convert_to_int(char))):
            print(char, ': ', decrypt(
                "TBIZLJB QL KFKBQV-BFDEQV-CLRO!", convert_to_int(char)))
            break


test()
