class Solution:

    def jump_game(self, nums):
        max_reachable = len(nums) - 1

        for i in range(len(nums) - 2, 0, -1):
            if i + nums[i] >= max_reachable:
                max_reachable = i

        return nums[0] >= max_reachable