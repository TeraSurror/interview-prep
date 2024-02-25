class Solution:
    def rob2(self, nums):
        if len(nums) == 1:
            return nums[0]
            
        nums1 = nums.copy()

        for i in range(1, len(nums) - 1):
            curr_val = nums[i] + (nums[i - 2] if i - 2 >= 0 else 0)
            nums[i] = max(curr_val, nums[i - 1])
        for j in range(len(nums1) - 2, 0, -1):
            curr_val = nums1[j] + (nums1[j + 2] if j + 2 < len(nums) else 0)
            nums1[j] = max(curr_val, nums1[j + 1])

        return max(nums1[1], nums[len(nums) - 2])


        


