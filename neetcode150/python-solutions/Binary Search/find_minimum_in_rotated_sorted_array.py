class Solution:
    def find_min(self, nums):
        L = 0
        R = len(nums) - 1
        result = float("inf")
        while L <= R:
            curr_min = L + ((R - L) // 2)
            result = min(result, nums[curr_min])
            if nums[curr_min] > nums[R]:
                L = curr_min + 1
            else:
                R = curr_min - 1

        return result
