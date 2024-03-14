from collections import deque


def getMaxEatenDishCount(N, D, K):

    result = 0

    dishes_q = deque([])
    dishes_set = set()

    for dish in D:
        if dish not in dishes_set:
            result += 1
            dishes_set.add(dish)
            dishes_q.append(dish)
            if len(dishes_q) == K + 1:
                d = dishes_q.popleft()
                dishes_set.remove(d)

    return result


print(getMaxEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2))
