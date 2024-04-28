# https://www.geeksforgeeks.org/problems/queue-reversal/1

from collections import deque
class Queue:
    def __init__(self):
        self.Queue=deque()
    def print(self):
        for i in self.Queue:
            print(i, end=' ')
    def enqueue(self,data):
        print(data)
        self.Queue.append(data)

    def dequeue(self):
        print(self.Queue[0])
        self.Queue.popleft()
    def reverse(self):
        s=list(self.Queue)
        k=s[::-1]
        for  i in k:
            print(i, end=' ')

if __name__ == '__main__':
    Q=Queue()
    Q.enqueue(12)
    Q.enqueue(11)
    Q.enqueue(1)
    Q.enqueue(12)
    Q.enqueue(41)
    print(Q.print())
    print(Q.reverse())

