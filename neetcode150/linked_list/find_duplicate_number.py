from typing import List


def find_duplicate_number(nums: List[int]) -> int:
    slow: int = 0
    fast: int = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break

    slow2: int = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return nums[slow]

    return -1
