class Solution:

    def jump_game_2(self, nums):

        dp = [float('inf')] * len(nums)
        dp[len(nums) - 1] = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]