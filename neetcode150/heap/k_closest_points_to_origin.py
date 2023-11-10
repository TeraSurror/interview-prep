import heapq
import math


class Solution:
    def closest_points(self, points, k):
        heap = []

        for point in points:
            distance = self.get_ed(point)
            heap.append((distance, point[0], point[1]))

        heapq.heapify(heap)

        result = []
        for _ in range(k):
            point = heapq.heappop(heap)
            result.append([point[1], point[2]])

        return result

    def get_ed(self, point):
        x = math.pow(point[0], 2)
        y = math.pow(point[1], 2)
        distance = math.sqrt(x + y)
        return distance
