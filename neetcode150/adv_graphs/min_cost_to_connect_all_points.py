from heapq import heappop, heappush


def min_cost(points):
    mapping = {point: i for i, point in enumerate(points)}

    point_list = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            a = points[i]
            b = points[j]
            dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
            heappush(point_list, (dist, mapping[a], mapping[b]))

    parent = [i for i in range(len(points))]
    rank = [1 for i in range(len(points))]

    def find(n):
        root = n
        while root != parent[root]:
            root = parent[root]

        while n != root:
            next = parent[n]
            parent[n] = root
            n = next

        return root

    def union(p1, p2):
        root1 = find(p1)
        root2 = find(p2)

        if root1 == root2:
            return False

        if rank[root1] < rank[root2]:
            rank[root2] += rank[root1]
            parent[root1] = root2
        else:
            rank[root1] += rank[root2]
            parent[root2] = root1

        return True

    result = 0
    while len(point_list) != 0:
        dist, a, b = heappop(point_list)
        if union(a, b):
            result += dist

    return result
