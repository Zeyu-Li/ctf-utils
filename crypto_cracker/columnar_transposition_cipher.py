from typing import List
import math
import itertools
from util import detect_english


def encrypt(plain_text: str, key: List[int] | int) -> str:
    if type(key) == int:
        key = list(range(key))

    columnar = ["" for _ in range(len(key))]

    for i, char in enumerate(plain_text):
        columnar[i % len(key)] += char

    result = ''
    for col in key:
        result += columnar[col - 1]

    return result


def decrypt(cipher_text: str, key) -> str:
    if type(key) == int:
        key = list(range(key))
    else:
        # convert to List[int] that is 0 indexed
        key = [i-1 for i in key]
    key_len = len(key)
    # get the len for each bucket
    text_len = len(cipher_text)
    bucket_size_margin = text_len % key_len
    bucket_count = text_len // key_len

    # get evenly divided bucket sizes
    size_stack = [bucket_count] * len(key)
    for i in range(bucket_size_margin):
        size_stack[i] += 1
    bucket_sizes = {}

    for i, item in enumerate(key):
        bucket_sizes[item] = size_stack[item]

    buckets = [""] * len(key)
    start_ptr = 0
    for key_item in key:
        buckets[key_item] = cipher_text[start_ptr:start_ptr+bucket_sizes[key_item]]
        start_ptr += bucket_sizes[key_item]

    result = ''
    # convert buckets back to original
    for i in range(max(size_stack)):
        for bucket in buckets:
            if len(bucket) > i:
                result += bucket[i]
    return result


def test():
    # unit tests
    max_range = 10
    key_range = [[1]]
    # iterate all position mixed column positions
    for i in range(1, 10):
        key_range += list(itertools.permutations(range(1, i + 1)))

    test_strings = ["IS HAUCREERNP F", "EL OLHLOWRD"]

    for test_string in test_strings:
        for key in key_range:
            if detect_english(decrypt(test_string, key)):
                print(key, ': ', decrypt(test_string, key))
                break


test()
