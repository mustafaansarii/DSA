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

    def dequeue(self, k):
        if len(self.queue) == 0:
            return "Queue is Empty!"
        else:
            for i in range(k):
                print(f"Element deleted from Queue is {self.queue[0]}")
                self.queue.popleft()


if __name__ == '__main__':
    Q = Queue(5)

    Q.Enqueue(10)
    Q.Enqueue(20)
    Q.Enqueue(30)
    Q.Enqueue(40)
    Q.Enqueue(50)

    Q.dequeue(3)
    print(Q._print()
)