# https://www.geeksforgeeks.org/implement-undo-and-redo-features-of-a-text-editor/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return new_node.data
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node
        return new_node.data

    def print(self):
        if self.head is None:
            return "Stack list is Empty!"
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next

    def pop(self):
        if self.head is None:
            raise IndexError("Empty! Stack")
        if self.head.next is None:
            popped_value = self.head.data
            self.head = self.head.next
            return popped_value
        n = self.head
        while n.next.next:
            n = n.next
        s = n.next.data
        n.next = None
        return s

    def undo_redo(self, S1, S2, text):
        for i in text:
            if i == "u":
                S2.push(S1.pop())
            elif i == "r":
                S1.push(S2.pop())
        return S1.print()

if __name__ == '__main__':
    stack1 = Stack()
    stack2 = Stack()

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.print()
    print()
    stack1.undo_redo(stack1, stack2, "uuurr")
