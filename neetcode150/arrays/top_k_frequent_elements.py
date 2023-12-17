import collections
import heapq


def top_k_frequent_elements(nums, k):
    freq = collections.defaultdict()

    for num in nums:
        freq[num] += 1

    heap = []
    for key, value in freq.items():
        heapq.heappush(heap, (-value, key))

    result = []
    for i in range(k):
        num = heapq.heappop(heap)
        result.push(num[1])

    return result
