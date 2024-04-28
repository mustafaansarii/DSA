# https://www.geeksforgeeks.org/array-implementation-of-queue-simple/
from collections import deque
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = deque()

    def _print(self):
        return self.queue

    def Enqueue(self, data):
        if self.size == len(self.queue):
            return "Queue is size Full can't insert!"
        print(f"Element added: {data}")
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is Empty!"
        else:
            print(f"Element deleted from Queue is {self.queue[0]}")
            self.queue.popleft()


if __name__ == '__main__':
    Q = Queue(5)

    Q.Enqueue(10)
    Q.Enqueue(20)
    Q.Enqueue(30)
    Q.Enqueue(40)
    Q.Enqueue(50)

    print(Q.Enqueue(60))

    Q.dequeue()
    Q.dequeue()
    Q.dequeue()

    print(Q._print())