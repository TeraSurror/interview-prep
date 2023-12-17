from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    start: int = 0
    end: int = len(numbers) - 1

    while start < end:
        total = numbers[start] + numbers[end]
        if target > total:
            start += 1
        elif target < total:
            end -= 1
        else:
            return [start, end]

    return [-1, -1]
