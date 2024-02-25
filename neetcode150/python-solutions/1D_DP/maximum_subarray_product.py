class Solution:
    def maxProduct(self, nums):

        result = nums[0]
        currMax = 1
        currMin = 1

        for num in nums:
            temp = currMax * num

            currMax = max(temp, currMin * num, num)
            currMin = min(temp, currMin * num, num)

            result = max(result, currMax)

        return result
