def product_except_self(nums):
    N = len(nums)
    result = [1] * N

    for i in range(1, N):
        result[i] = result[i - 1] * nums[i - 1]

    postfix = 1

    for i in range(N - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
