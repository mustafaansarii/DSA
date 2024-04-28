from collections import deque


class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    def _print(self):
        if len(self.queue) == 0:
            return self.queue
        for i in range(len(self.queue)):
            print(self.queue[i], end=' ')

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


Q = Queue(5)

if __name__ == '__main__':

    print(Q._print())