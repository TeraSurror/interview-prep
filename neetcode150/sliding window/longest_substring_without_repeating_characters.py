from typing import Set


def length_of_longest_substring(s: str) -> int:
    result: int = 0
    left: int = 0
    characters: Set[str] = set()

    for right in range(len(s)):
        while s[right] in characters:
            characters.remove(s[left])
            left += 1
        characters.add(s[right])
        result = max(result, right - left + 1)

    return result
