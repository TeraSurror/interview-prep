def subsets(nums):
    result = []
    nums.sort()

    def dfs(i, subsets):
        if i >= len(nums):
            result.append(subsets[::])
            return

        subsets.append(nums[i])
        dfs(i + 1, subsets)
        subsets.pop()

        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1

        dfs(i + 1, subsets)

    dfs(0, [])
    return result
