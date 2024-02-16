from string import ascii_uppercase
import math

ascii_withspace = ascii_uppercase + ' '


def gcd(num1: int, num2: int) -> int:
    return math.gcd(num1, num2)


def get_dictionary(file="../dictionary/dictionary.txt"):
    with open(file, 'r') as fp:
        return [line.strip() for line in fp.readlines()]


def detect_english(text: str, word_percentage=20, letter_percentage=85) -> bool:
    words = get_dictionary()
    word_match = 0
    text = text.upper()

    word_string = ''
    for char in text:
        if char in ascii_withspace:
            word_string += char

    word_list = word_string.split()
    for word in word_list:
        if word in words:
            word_match += 1

    word_match = word_match / len(word_list) * 100

    letter_match = 0

    for char in text:
        letter_match += 1 if char in ascii_withspace else 0

    letter_match = letter_match / len(text) * 100

    return (word_match > word_percentage) and (letter_match > letter_percentage)

# from https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def sieve_of_eratosthenes(t):
    sieve = [True for _ in range(t+1)]
    sieve[0] = sieve[1] = False
    for i in range(2, int(t**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, t + 1, i):
                sieve[j] = False
    return [x for x in range(t + 1) if sieve[x]]
