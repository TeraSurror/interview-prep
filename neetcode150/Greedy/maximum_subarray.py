class Solution:
    def maximum_sum(self, nums):

        max_sum = float('-inf')
        curr_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum += max(curr_sum, curr_sum + nums[i])
            max_sum += max(max_sum, curr_sum)

        return max_sum
            