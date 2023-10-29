class Solution:

    def find_ways_dp(self, nums, target):
        dp = dict()
        def recurse(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0
            if (index, curr_sum) in dp:
                return dp[(index, curr_sum)]               
            
            dp[(index, curr_sum)] = recurse(index + 1, curr_sum + nums[index]) + recurse(index + 1, curr_sum - nums[index])

            return dp[(index, curr_sum)]            
        
        result = recurse(0, 0)
        return result

    def find_ways_recursive(self, nums, target):
        def recurse(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            
            result = recurse(index + 1, total + nums[index]) + recurse(index + 1, total - nums[index])

            return result

        return recurse(0, 0)