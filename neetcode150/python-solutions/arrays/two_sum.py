def two_sum(nums, target):
    diff = {}

    for i in range(len(nums)):
        if nums[i] in diff:
            return [i, diff[nums[i]]]
        else:
            diff[target - nums[i]] = i

    return [-1, -1]
