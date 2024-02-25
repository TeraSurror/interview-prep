def palindrome_partitioning(s):
    result = []

    curr_part = []

    def dfs(i):
        if i >= len(s):
            result.append(curr_part[:])
            return

        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                curr_part.append(s[i : j + 1])
                dfs(j + 1)
                curr_part.pop()

    def is_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    dfs(0)

    return result
