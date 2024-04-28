# https://www.geeksforgeeks.org/implement-stack-queue-using-deque/

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None

class DQueue:
    def __init__(self):
        self.head = None

    def Enqueue_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def Enqueue_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def _print(self):
        if self.head is None: return "Queue is Empty!"
        n = self.head
        while n is not None:
            print(n.data, end=' ')
            n = n.next

    def Deque_begin(self):
        if self.head is None: return "Queue is Empty!"
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next

    def Deque_end(self):
        if self.head is None: return "Queue is Empty!"
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None


class stack:
    def __init__(self):
        self.stack = DQueue()

    def insert(self, data):
        self.stack.Enqueue_begin(data)

    def Remove(self):
        self.stack.Deque_begin()

    def print_stack(self):
        self.stack._print()


class Queue:
    def __init__(self):
        self.Queue = DQueue()

    def Enqueue(self, data):
        self.Queue.Enqueue_end(data)

    def dequeue(self):
        self.Queue.Deque_begin()

    def print_q(self):
        self.Queue._print()

if __name__ == '__main__':
    s = stack()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    print("Stack: ")
    s.print_stack()  # Output: 3 2 1
    s.Remove()
    print("\nAfter popping:")
    s.print_stack()  # Output: 2 1

    # Now, let's test the queue
    q = Queue()
    q.Enqueue(2)
    q.Enqueue(6)
    q.Enqueue(3)
    print("\nQueue:")
    q.print_q()  # Output: 1 2 3
    q.dequeue()
    print("\nAfter dequeuing:")
    q.print_q()  # Output: 2 3


