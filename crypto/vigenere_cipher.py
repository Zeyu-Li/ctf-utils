import string


LETTERS = string.ascii_uppercase

"""
util function to convert char key to int
"""
def convert_to_int(key):
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

def encrypt(plain_text: str, key: str) -> str:
    # convert everything to uppercase
    plain_text = plain_text.upper()
    key = key.upper()
    result_text = ''
    key_ptr = 0
    for char in plain_text:
        if char in LETTERS:
            result_text += LETTERS[(LETTERS.index(char) + convert_to_int(key[key_ptr])) % 26]
            key_ptr = (key_ptr + 1) % len(key)
        else:
            result_text += char
    
    return result_text

def decrypt(cipher_text: str, key: str) -> str:
    # convert key to negative of the key to work backwards and feed it in to feed forward
    new_key = ''
    for char in key:
        new_key += LETTERS[(26-convert_to_int(char)) % 26]
    return encrypt(cipher_text, new_key)

def test():
    # unit tests
    assert encrypt("401.", 'b') == "401."
    assert encrypt("401.", 'aaaaaaaa') == "401."
    assert encrypt("401.", 'a') == "401."
    assert encrypt("401.", 'z') == "401."
    assert encrypt("Hello World!", 'aaaaaaaaaaaaa') == "Hello World!".upper()
    assert encrypt("Hello World!", 'a') == "Hello World!".upper()
    assert encrypt("Hello World!", 'b') == "Ifmmp Xpsme!".upper()
    assert encrypt("I'm late for work and my car isn't working, so I need to find someone to take me to work.", 'secret') == "A'q nrxx xst nskc epu qr uet zwg'l aqiobfk, uf M gwif ks yarf jsfwspv xh lemv qx ls yfvd.".upper()
    assert encrypt("Hello World!", 'z') == "Gdkkn Vnqkc!".upper()
    
    
    assert decrypt("401.", 'b') == "401."
    assert decrypt("401.", 'aaaaaaaa') == "401."
    assert decrypt("401.", 'a') == "401."
    assert decrypt("401.", 'z') == "401."
    assert decrypt("Hello World!", 'a') == "Hello World!".upper()
    assert decrypt("Ifmmp Xpsme!", 'b') == "Hello World!".upper()
    assert decrypt("A'q nrxx xst nskc epu qr uet zwg'l aqiobfk, uf M gwif ks yarf jsfwspv xh lemv qx ls yfvd.", 'SECRET') == "I'm late for work and my car isn't working, so I need to find someone to take me to work.".upper()
    assert decrypt("Gdkkn Vnqkc!", 'z') == "Hello World!".upper()

test()
