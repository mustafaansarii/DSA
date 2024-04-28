# https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def _print(self):
        if self.head is None:
            return "Stack list is Empty!"
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next
            print()

    def Remove_last(self):
        if self.head is None:
            return "Stack list is Empty!"
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next


stack = Stack()

if __name__ == '__main__':
    stack.insert_begin(1)
    stack.insert_begin(2)
    stack.insert_begin(3)
    stack.insert_begin(4)
    stack._print()
    stack.Remove_last()