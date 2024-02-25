import heapq


class Solution:
    def last_stone_weight(self, stones):
        new_stones = [-num for num in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            a = -1 * heapq.heappop(new_stones)
            b = -1 * heapq.heappop(new_stones)
            if a != b:
                heapq.heappush(new_stones, -1 * abs(a - b))

        return 0 if not new_stones else -1 * new_stones[0]
