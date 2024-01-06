from typing import List

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

def decrypt(cipher_text: str, keyA: int, keyB: int) -> str:
    cipher_text = cipher_text.upper()
    
    plaintext = ''
    for char in cipher_text:
        if char in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(char)
            plaintext += SYMBOLS[(symbolIndex - keyB) * pow(keyA, -1, len(SYMBOLS)) % len(SYMBOLS)]
        else:
            plaintext += char
    
    return plaintext

def test():
    # unit tests
    assert encrypt("Hello World!", 15, 5) == "Gnooh Xhaoy!".upper()
    assert encrypt("Hello World!", 5, 15) == "Yjssh Vhwse!".upper()
    assert encrypt("aaaaaaaaaaaaa", 3, 0) == "aaaaaaaaaaaaa".upper()
    
    assert decrypt("Gnooh Xhaoy!", 15, 5) == "Hello World!".upper()
    assert decrypt("Yjssh Vhwse!", 5, 15) == "Hello World!".upper()
    assert decrypt("aaaaaaaaaaaaa", 3, 0) == "aaaaaaaaaaaaa".upper()

test()