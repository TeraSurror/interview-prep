def getMinCodeEntryTime(N, M, C):
    start = 1
    total = 0

    for dest in C:
        total += min(((dest - start) % N), ((start - dest) % N))
        start = dest

    return total
