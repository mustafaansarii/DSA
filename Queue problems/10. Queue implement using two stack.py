
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def print(self):
        for i in self.stack:
            print(i, end=' ')

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return "Empty! stack"
        return self.stack.pop()  # Return the popped element

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, data):
        while self.dequeue_stack.size() > 0:
            self.enqueue_stack.push(self.dequeue_stack.pop())
        self.enqueue_stack.push(data)

    def dequeue(self):
        while self.enqueue_stack.size() > 0:
            self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue elements:")
    print("\nDequeuing elements:")
    print(q.dequeue())  # Output: 10
    print(q.dequeue())  # Output: 20
    print(q.dequeue())  # Output: 30
    print(q.dequeue())  # Output: Empty! Stack