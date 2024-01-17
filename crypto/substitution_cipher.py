import string
from typing import Dict


LETTERS = string.ascii_uppercase


def encrypt(plain_text: str, key: Dict[str, str] | str) -> str:
    """substitution cipher the plain_text

    Args:
        plain_text (str): the plain text to be encrypted
        key (Dict[str, str] | str): key can either be a direct mapping for each letter or single 26 character string that the letters maps onto

    Returns:
        str: the cipher text
    """
    # convert everything to uppercase
    plain_text = plain_text.upper()
    result_text = ''
    if isinstance(key, str):
        key = key.upper()

        assert len(key) == 26, "The key must have length 26 one for each letter"
        for char in plain_text:
            if char in LETTERS:
                result_text += key[LETTERS.index(char)]
            else:
                result_text += char
    else:
        assert isinstance(
            key, dict), "The key is not valid, must be a str or dictionary for each character in alphabet"
        assert len(
            key) == 26, "The key must have 26 key, values, one for each letter onto another"

        for char in plain_text:
            if char in key:
                result_text += key[char]
            elif char.lower() in key:
                result_text += key[char.lower()]
            elif char.upper() in key:
                result_text += key[char.upper()]
            else:
                result_text += char

    return result_text


def decrypt(cipher_text: str, key: Dict[str, str] | str) -> str:
    # swap the key
    return encrypt(cipher_text, key)


def test():
    default_mapping = {}
    for i, j in zip(LETTERS, LETTERS):
        default_mapping[i] = j

    # reverse
    reverse_letters = LETTERS[::-1]
    reverse_mapping = {}
    for i, j in zip(LETTERS, LETTERS[::-1]):
        reverse_mapping[i] = j

    # unit tests
    assert encrypt("401.", LETTERS) == "401."
    assert encrypt("401.", default_mapping) == "401."
    assert encrypt("401.", reverse_letters) == "401."
    assert encrypt("401.", reverse_mapping) == "401."
    assert encrypt("Hello World!", LETTERS) == "Hello World!".upper()
    assert encrypt("Hello World!", default_mapping) == "Hello World!".upper()
    assert encrypt("Hello World!", reverse_letters) == "SVOOL DLIOW!".upper()
    assert encrypt("Hello World!", reverse_mapping) == "SVOOL DLIOW!".upper()

    assert decrypt("401.", LETTERS) == "401."
    assert decrypt("401.", default_mapping) == "401."
    assert decrypt("401.", reverse_letters) == "401."
    assert decrypt("401.", reverse_mapping) == "401."
    assert decrypt("Hello World!", LETTERS) == "Hello World!".upper()
    assert decrypt("Hello World!", default_mapping) == "Hello World!".upper()
    assert decrypt("SVOOL DLIOW!", reverse_letters) == "Hello World!".upper()
    assert decrypt("SVOOL DLIOW!", reverse_mapping) == "Hello World!".upper()


test()
