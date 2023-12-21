from collections import defaultdict
from typing import Dict, Set


def character_replacement(s: str, k: int) -> int:
    result: int = 0
    max_length: int = 0
    left: int = 0
    char_set: Dict[str, int] = defaultdict(int)

    for right in range(len(s)):
        char_set[s[right]] += 1
        max_length = max(max_length, char_set[s[right]])

        while (right - left + 1) - max_length > k:
            char_set[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result
