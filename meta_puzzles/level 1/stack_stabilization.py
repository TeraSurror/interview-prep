def getMinimumDeflatedDiscount(N, R):
    count = 0

    for i in range(len(R) - 2, -1, -1):
        if R[i] >= R[i + 1]:
            new_val = R[i + 1] - 1
            if new_val <= 0:
                return -1
            R[i] = new_val
            count += 1

    return count
