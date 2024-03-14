import math
from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    num_diners: int = (S[0] - 1) // (K + 1)

    for i in range(1, len(S)):
        num_diners += (S[i] - S[i - 1] - K - 1) // (K + 1)

    num_diners += (N - S[-1]) // (K + 1)

    return num_diners


print(getMaxAdditionalDinersCount(10, 1, 2, [2, 6]))
