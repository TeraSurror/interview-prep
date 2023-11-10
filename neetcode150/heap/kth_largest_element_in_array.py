import heapq


class Solution:
    def kth_largest(self, nums, k):
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
