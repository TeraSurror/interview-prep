from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    nums.sort()

    for i, num in enumerate(nums):
        if num > 0:
            break
        if i > 0 and num == nums[i - 1]:
            continue

        l: int = i + 1
        r: int = len(nums) - 1
        while l < r:
            total = num + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result
