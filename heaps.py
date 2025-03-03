import heapq


# heaps under the hood are implemented as arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 55)
heapq.heappush(minHeap, 7)
heapq.heappush(minHeap, 6)
print(minHeap)
# min is always in index 0

# loop through a heap
while len(minHeap):
    print(minHeap)
    print(heapq.heappop(minHeap))

print("my heap ::".format(minHeap))

# no max heap by default, we just multiply by -1

# build heap is called heapify in python 
arr = [2,1,8,4,7]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))