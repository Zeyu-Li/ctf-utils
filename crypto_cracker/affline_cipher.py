from typing import List
from util import get_dictionary, detect_english, gcd

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
Check if keyA and keyB are valid for a unique encoding with the symbols
"""


def check_unique(keyA: int, keyB: int) -> bool:
    mappings = []
    for i, _ in enumerate(SYMBOLS):
        map_ = i * keyA + keyB
        if map_ in mappings:
            return False
        mappings.append(map_)
    return True


def encrypt(plain_text: str, keyA: int, keyB: int) -> str:
    plain_text = plain_text.upper()

    result = ""
    for char in plain_text:
        if char in SYMBOLS:
            transfered = (SYMBOLS.index(char) * keyA + keyB) % 26
            result += SYMBOLS[transfered]
        else:
            result += char

    return result


def decrypt(cipher_text: str, keyA: int, keyB: int, check_valid=False) -> str:
    if check_valid:
        if gcd(keyA, len(SYMBOLS)) != 1:
            raise ArithmeticError(
                "keyA results in conflicting values for some character")

    cipher_text = cipher_text.upper()

    plaintext = ''
    for char in cipher_text:
        if char in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(char)
            plaintext += SYMBOLS[(symbolIndex - keyB) *
                                 pow(keyA, -1, len(SYMBOLS)) % len(SYMBOLS)]
        else:
            plaintext += char

    return plaintext


def get_key_parts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def test():
    key_range = range(len(SYMBOLS) ** 2)
    # unit tests
    test_strings = ["Gnooh Xhaoy!", "Yjssh Vhwse!"]
    for test_string in test_strings:
        for key in key_range:
            keyA, keyB = get_key_parts(key)
            # check if gcd
            if gcd(keyA, len(SYMBOLS)) != 1:
                continue
            if detect_english(decrypt(test_string, keyA, keyB)):
                print(keyA, keyB, ': ', decrypt(test_string, keyA, keyB))
                break

    # assert decrypt("Gnooh Xhaoy!", 15, 5) == "Hello World!".upper()
    # assert decrypt("Yjssh Vhwse!", 5, 15) == "Hello World!".upper()


test()
