#https://www.geeksforgeeks.org/reverse-a-stack-using-queue/

from collections import deque


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = deque()

    def insert(self, data):
        print(f"element inserted in stack: {data}")
        return self.stack.append(data)

    def _print(self):
        if len(self.stack) == 0:
            return "stack is Empty!"
        for i in range(len(self.stack)):
            print(self.stack[i])

    def Remove(self):
        if len(self.stack) == 0:
            return "stack is Empty!"
        return self.stack.pop()


R = Stack(5)


class Queue:
    def __init__(self):
        self.Queue = deque()

    def Enqueue(self, data):
        print(f"element inserted in Queue: {data}")
        return self.Queue.append(data)

    def _print(self):
        if len(self.Queue) == 0:
            return "Queue is Empty!"
        for i in range(len(self.Queue)):
            print(self.Queue[i], end=' ')

    def Dequeue(self):
        if len(self.Queue) == 0:
            return "Queue is Empty!"
        return self.Queue.popleft()


Qu = Queue()


class Reverse_Stack:
    def Remove_from_stack_insert_into_queue(self):
        while len(R.stack) != 0:
            Qu.Enqueue(R.Remove())
        return Qu._print()

    def Remove_from_queue_insert_into_stack(self):
        while len(Qu.Queue) != 0:
            R.insert(Qu.Dequeue())
        return R._print()

if __name__ == '__main__':
    R = Stack(5)

    R.insert(1)
    R.insert(2)
    R.insert(3)
    R.insert(4)
    R.insert(5)

    rv = Reverse_Stack()

    rv.Remove_from_stack_insert_into_queue()

    rv.Remove_from_queue_insert_into_stack()

    R._print()

    R = Stack(5)

    R.insert(1)
    R.insert(2)
    R.insert(3)
    R.insert(4)
    R.insert(5)

    print("---------------------")

    R._print()
