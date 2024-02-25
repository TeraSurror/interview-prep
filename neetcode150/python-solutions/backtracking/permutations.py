from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    def generate_permutations(index):
        if index == len(nums) - 1:
            result.append(nums[:])

        for j in range(index, len(nums)):
            nums[j], nums[index] = nums[index], nums[j]
            generate_permutations(index + 1)
            nums[index], nums[j] = nums[j], nums[index]

    result = []
    generate_permutations(0)
    return result
