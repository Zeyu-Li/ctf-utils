import string


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
    # unit tests
    assert encrypt("401.", 1) == "401."
    assert encrypt("401.", 3) == "401."
    assert encrypt("401.", 300) == "401."
    assert encrypt("401.", -1) == "401."
    assert encrypt("Hello World!", 0) == "Hello World!".upper()
    assert encrypt("Hello World!", 26) == "Hello World!".upper()
    assert encrypt("Hello World!", 1) == "Ifmmp Xpsme!".upper()
    assert encrypt("Hello World!", 300) == "Vszzc Kcfzr!".upper()
    assert encrypt("Hello World!", -1) == "Gdkkn Vnqkc!".upper()
    
    
    assert decrypt("401.", 1) == "401."
    assert decrypt("401.", 3) == "401."
    assert decrypt("401.", 300) == "401."
    assert decrypt("401.", -1) == "401."
    assert decrypt("Hello World!", 0) == "Hello World!".upper()
    assert decrypt("Hello World!", 26) == "Hello World!".upper()
    assert decrypt("Ifmmp Xpsme!", 1) == "Hello World!".upper()
    assert decrypt("Vszzc Kcfzr!", 300) == "Hello World!".upper()
    assert decrypt("Gdkkn Vnqkc!", -1) == "Hello World!".upper()

test()
