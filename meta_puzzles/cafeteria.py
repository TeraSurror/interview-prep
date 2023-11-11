from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    occ = [0] * N

    for i in S:
        occ[i - 1] = 1

        left = i
        right = i - 2
        j = 0

        while j < K:
            if left >= 0:
                occ[left] = -1
                left -= 1
            if right < N:
                occ[right] = -1
                right += 1
            j += 1

    def dfs(index):
        if index == N:
            return 0

    return 0


getMaxAdditionalDinersCount(10, 1, 2, [2, 6])
