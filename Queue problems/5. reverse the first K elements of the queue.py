#https://www.geeksforgeeks.org/reversing-first-k-elements-queue/

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    def _print(self):
        return self.queue

    def Enqueue(self, data):
        print(f"Element added: {data}")
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is Empty!"
        else:
            print(f"Element deleted from Queue is {self.queue[0]}")
            self.queue.popleft()

    def ReverseK(self, K):
        if K <= 0:
            return "Invalid value of K"
        for i in range(K // 2):
            self.queue[i], self.queue[K - i - 1] = self.queue[K - i - 1], self.queue[i]
        return self.queue


Q = Queue()
if __name__ == '__main__':
    Q.Enqueue(110)
    Q.dequeue()
    print(Q._print())
    print(Q.ReverseK(5))
