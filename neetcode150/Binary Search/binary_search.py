class Solution:
    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = ((end - start) // 2) + start

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
