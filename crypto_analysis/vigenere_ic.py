def string_IC(text: str) -> float:
    # base case
    if len(text) == 1: return 1
    character_map = dict()
    
    for char in text:
        character_map[char] = character_map.get(char, 0) + 1
        
    t_sum = 0
    for v in character_map.values():
        t_sum += v * (v-1)
    
    return t_sum / (len(text) * (len(text) - 1))


def subseq_IC(cipher_text: str, key_len: int) -> float:
    """
    Return the average IC of text for 
    subsequences induced by a given a key length
    """
    ic_set = []
    for _ in range(key_len):
        ic_set.append('')
    for i in range(len(cipher_text)):
        ic_set[i % key_len] += cipher_text[i]
    
    total = 0
    for ic in ic_set:
        total += string_IC(ic)
    return total/key_len

def keyscore_IC(cipher_text: str, n: int, max_len = 20):
    """Catches the top n possible key lengths

    Args:
        cipher_text (str): _description_
        n (int): _description_
        max_len (int, optional): _description_. Defaults to 20.
        
    Return:
        (List[int]): top n possible key lengths
    """

    probabilities = dict()
    
    for i in range(1, min(len(cipher_text), max_len + 1)):
        probabilities[i] = subseq_IC(cipher_text, i)
    
    sorted_probability = list(sorted(probabilities.items(), key=lambda x:x[1], reverse=True))
    res = []
    for i in range(len(sorted_probability)):
        if i >= n: break
        # print(sorted_probability[i][0])
        res.append(sorted_probability[i][0])
    # print(res)
    return res

def test():
    assert string_IC("CDC") == 1/3
    assert keyscore_IC('PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU', 5) == [8, 16, 4, 12, 6]

test()