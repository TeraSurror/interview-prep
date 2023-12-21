from typing import Dict


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    len_s1: int = len(s1)
    len_s2: int = len(s2)

    for i in range(len_s1 - 1, len_s2):
        sub_str: str = s2[i - len_s1 + 1 : i + 1]
        if is_permutation(sub_str, s1):
            return True

    return False


def is_permutation(s1: str, s2: str) -> bool:
    s1_dict: Dict[str, int] = {}

    for letter in s1:
        s1_dict[letter] = 1 + s1_dict.get(letter, 0)

    for letter in s2:
        if letter not in s1_dict:
            return False
        s1_dict[letter] -= 1
        if s1_dict[letter] == 0:
            del s1_dict[letter]

    return True
