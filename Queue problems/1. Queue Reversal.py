# https://www.geeksforgeeks.org/problems/queue-reversal/1
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue.popleft()

    def print_reverse(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        reversed_queue = deque(reversed(self.queue))
        for item in reversed_queue:
            print(item, end=" ")
        print()

    def size(self):
        return len(self.queue)
        
    def print(self):
        for i in self.queue:
            print(i,end=' ')


Q=Queue()
