# https://leetcode.com/problems/implement-stack-using-queues/description/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def dequeu(self):
        if self.head is None:
            return "Queue is Empty!"
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            p = n
            n = n.next
        p.next = None

    def _print(self):
        if self.head is None:
            return "Queue is Empty!"
        n = self.head
        while n is not None:
            print(n.data, end=' ')
            n = n.next


class stack:
    def __init__(self):
        self.Stack=Queue()

    def insert(self,data):
        self.Stack.enqueue(data)

    def pop(self):
        if self.Stack.head is None:
            return "Stack is Empty!"
        self.Stack.head = self.Stack.head.next

    def _print(self):
        self.Stack._print()

if __name__ == '__main__':
    my_stack = stack()

    my_stack.insert(5)
    my_stack.insert(10)
    my_stack.insert(15)

    print("Stack elements:")
    my_stack._print()
    popped_element = my_stack.pop()
    print("\nStack elements after popping:")
    my_stack._print()


