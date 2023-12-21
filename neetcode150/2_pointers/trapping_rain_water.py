def trap(height):
    if not height:
        return 0

    result = 0

    left = 0
    right = len(height) - 1
    maxLeft = height[left]
    maxRight = height[right]

    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            result += max(maxLeft - height[left], 0)
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            result += max(maxRight - height[right], 0)

    return result
