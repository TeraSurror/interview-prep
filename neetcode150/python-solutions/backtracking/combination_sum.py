from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []

    curr_elements: List[int] = []

    def dfs(i: int, aim: int) -> None:
        if aim == 0:
            result.append(curr_elements.copy())

        for j in range(i, len(candidates)):
            if aim - candidates[j] >= 0:
                curr_elements.append(candidates[j])
                dfs(j, aim - candidates[j])
                curr_elements.pop()

    dfs(0, target)

    return result
