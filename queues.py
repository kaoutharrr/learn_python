# queues are double ended by default in python

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)
queue.appendleft(2)
print(queue)
