from typing import Dict, List


def min_window(s: str, t: str):
    if t == "":
        return ""

    count_T: Dict[str, int] = {}
    window: Dict[str, int] = {}

    for letter in t:
        count_T[letter] = 1 + count_T.get(letter, 0)

    result = [-1, -1]
    result_length: float = float("infinity")
    have: int = 0
    need: int = len(count_T)

    left: int = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)

        if c in count_T and window[c] == count_T[c]:
            have += 1

        while have == need:
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = right - left + 1
            window[s[left]] -= 1

            if s[left] in count_T and window[s[left]] < count_T[s[left]]:
                have -= 1

            left += 1

    return s[result[0] : result[1] + 1] if result_length != float("infinity") else ""
