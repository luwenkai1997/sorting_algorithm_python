import heapq
import random


def topk(li, k):
    heap = li[0:k]
    heapq.heapify(heap)
    for i in li[k:]:
        if i > heap[0]:
            heap[0] = i
            heapq.heapify(heap)

    sorted_heap = []
    for j in range(len(heap)):
        sorted_heap.append(heapq.heappop(heap))
    return sorted_heap


li = random.sample(range(1000), 300)
print(topk(li, 10))


