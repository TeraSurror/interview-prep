from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []

    curr_subset: List[int] = []

    def dfs(i: int) -> None:
        if i >= len(nums):
            res.append(curr_subset.copy())
            return

        curr_subset.append(nums[i])
        dfs(i + 1)

        curr_subset.pop()
        dfs(i + 1)

    dfs(0)

    return res
