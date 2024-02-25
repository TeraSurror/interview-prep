class Solution:

    def max_coins(self, nums):

        def dfs(curr_result, temp_nums):

            if len(temp_nums) == 0:
                return curr_result
            
            res = 0
            for i in range(len(temp_nums)):
                prev = temp_nums[i - 1] if i - 1 >= 0 else 1
                next = temp_nums[i + 1] if i + 1 < len(temp_nums) else 1
                burst_val = temp_nums[i] + prev + next
                temp_nums.pop(i)
                res += dfs(i, burst_val, )

            return res

        return dfs(0, nums)
