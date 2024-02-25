class Solution:
    def countSubstrings(self, s: str) -> str:
        res = 0
        for i in range(len(s)):
            count = 0
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
            res += count

        return res

        