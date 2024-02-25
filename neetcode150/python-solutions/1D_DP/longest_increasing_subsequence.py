class Solution:
    def length_of_lis(self, nums):

        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)