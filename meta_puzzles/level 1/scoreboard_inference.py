def getMinProblemCount(N, S):
    num_2_points = S[0] // 2
    num_1_points = S[0] % 2

    for i in range(1, len(S)):
        new_n2p = S[i] // 2
        new_n1p = S[i] % 2

        if new_n2p > num_2_points:
            num_2_points = new_n2p
        if new_n1p > num_1_points:
            num_1_points = new_n1p

    return num_2_points + num_1_points
