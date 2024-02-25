from collections import Counter, deque
import heapq


class Solution:
    def task_scheduler(self, tasks, n):
        task_count = Counter(tasks)
        heap = [-count for count in task_count.values()]
        heapq.heapify(heap)

        q = deque([])
        time = 0

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                count = heapq.heappop(heap) + 1
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time
