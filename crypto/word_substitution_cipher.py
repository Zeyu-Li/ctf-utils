import string
from typing import Dict
from substitution_cipher import encrypt as substitution_encrypt


LETTERS = string.ascii_uppercase


def encrypt(plain_text: str, codebook: dict, key: Dict[str, str] | str) -> str:
    """substitution cipher the plain_text

    Args:
        plain_text (str): the plain text to be encrypted
        key (Dict[str, str] | str): key can either be a direct mapping for each letter or single 26 character string that the letters maps onto

    Returns:
        str: the cipher text
    """
    # convert with codebook first
    words = plain_text.split()
    codebook_encode = []

    for word in words:
        if word in codebook:
            codebook_encode.append(codebook[word])
        elif word.lower() in codebook:
            codebook_encode.append(codebook[word.lower()])
        elif word.upper() in codebook:
            codebook_encode.append(codebook[word.upper()])
        else:
            codebook_encode.append(word)

    return substitution_encrypt(' '.join(codebook_encode), key)


def decrypt(cipher_text: str, codebook: dict, key: Dict[str, str] | str) -> str:
    codebook_encoded = substitution_encrypt(cipher_text, key)

    # decode from codebook
    words = codebook_encoded.split()
    codebook_encode = []
    codebook = {v: k for k, v in codebook.items()}

    for word in words:
        if word in codebook:
            codebook_encode.append(codebook[word])
        elif word.lower() in codebook:
            codebook_encode.append(codebook[word.lower()])
        elif word.upper() in codebook:
            codebook_encode.append(codebook[word.upper()])
        else:
            codebook_encode.append(word)

    return ' '.join(codebook_encode)


def test():
    default_mapping = {}
    for i, j in zip(LETTERS, LETTERS):
        default_mapping[i] = j

    # reverse
    reverse_letters = LETTERS[::-1]
    reverse_mapping = {}
    for i, j in zip(LETTERS, LETTERS[::-1]):
        reverse_mapping[i] = j

    codebook = {
        "university": '1',
        "hello": '3',
    }

    # unit tests
    assert encrypt("401.", codebook, LETTERS) == "401."
    assert encrypt("401.", codebook, default_mapping) == "401."
    assert encrypt("401.", codebook, reverse_letters) == "401."
    assert encrypt("401.", codebook, reverse_mapping) == "401."
    assert encrypt("Hello World!", codebook, LETTERS) == "3 World!".upper()
    assert encrypt("Hello World!", codebook,
                   default_mapping) == "3 World!".upper()
    assert encrypt("Hello World!", codebook,
                   reverse_letters) == "3 DLIOW!".upper()
    assert encrypt("Hello World!", codebook,
                   reverse_mapping) == "3 DLIOW!".upper()

    assert decrypt("401.", codebook, LETTERS) == "401."
    assert decrypt("401.", codebook, default_mapping) == "401."
    assert decrypt("401.", codebook, reverse_letters) == "401."
    assert decrypt("401.", codebook, reverse_mapping) == "401."
    assert decrypt("3 World!", codebook,
                   LETTERS).upper() == "Hello World!".upper()
    assert decrypt("3 World!", codebook,
                   default_mapping).upper() == "Hello World!".upper()
    assert decrypt("3 DLIOW!", codebook,
                   reverse_letters).upper() == "Hello World!".upper()
    assert decrypt("3 DLIOW!", codebook,
                   reverse_mapping).upper() == "Hello World!".upper()


test()
