# https://www.geeksforgeeks.org/reverse-a-linked-list/

# https://www.geeksforgeeks.org/reverse-a-linked-list/

# https://www.geeksforgeeks.org/reverse-a-linked-list/

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Sll:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def _print(self):
        if self.head is None: return "LL Empty!"
        n = self.head
        while n is not None:
            print(n.data, end=' ')
            n = n.next

    def insert_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.push_begin(x)
            return
        self.tail.next = new_node
        self.tail = new_node

    def Reverse(self):
        if self.head is None:
            return "LL Empty!"
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return prev

    def rotate(self, k):
        pass

    def clear(self):
        self.head = None

if __name__ == '__main__':
    S=Sll()
    S.clear()
    S.push_begin(2)
    S.push_begin(4)
    S.push_begin(7)
    S.push_begin(8)
    S.push_begin(9)
    S.insert_end(1)
    S.insert_end(6)
    S.insert_end(5)
    S.insert_end(4)
    S._print()
