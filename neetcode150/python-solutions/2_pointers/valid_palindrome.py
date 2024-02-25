def is_palindrome(s: str) -> bool:
    s = s.lower()
    start: int = 0
    end: int = len(s) - 1

    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            return False

    return True
