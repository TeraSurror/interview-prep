from typing import List


def max_area(height: List[int]):
    result: int = 0

    start: int = 0
    end: int = len(height) - 1

    while start < end:
        curr_area = (end - start) * min(height[start], height[end])
        result = max(curr_area, result)

        if height[end] > height[start]:
            start += 1
        else:
            end -= 1

    return result
