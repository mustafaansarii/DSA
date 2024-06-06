class Node:
    def __init__(self,data):
        self.data=data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            n = self.head
            while n:
                print(n.data, end=' ')
                n = n.next

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.tail = None
        else:
            n = self.head
            while n.next.next:
                n = n.next
            data = n.next.data
            n.next = None
            self.tail = n
        return data


if __name__ == '__main__':
    S=Stack()
    arr=[10, 20, 30, 40, 50]
    for i in arr:
        S.push(i)
    reversed_arr = []
    for i in range(len(arr)):
        reversed_arr.append(S.pop())

