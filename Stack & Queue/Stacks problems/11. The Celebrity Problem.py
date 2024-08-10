# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays,Strings,Linked%20List&difficulty=Easy&sortBy=submissions
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

    def size(self):
        if self.head is None: return 0
        count = 0
        n = self.head
        while n:
            count += 1
            n = n.next
        return count

    def undo_redo(self, S1, S2, text):
        for i in text:
            if i == "u":
                S2.push(S1.pop())
            elif i == "r":
                S1.push(S2.pop())
        return S1.print()

    def __getitem__(self, index):
        n = self.head
        count = 0
        while n:
            if count == index:
                return n.data
            count += 1
            n = n.next
        raise IndexError("Index out of range")

    def celebrity(self, M, n):
        j = len(M[0])
        for i in range(j):
            c = 0
            for k in range(n):
                if M[k][i] == 1:
                    c += 1
            if c == n - 1:
                if M[i].count(0) == j:
                    return i
        return -1


if __name__ == '__main__':
    M = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    n = len(M)

    stack = Stack()

    celebrity_index = stack.celebrity(M,n)

    if celebrity_index != -1:
        print("Celebrity found at index:", celebrity_index)
    else:
        print("No celebrity found.")
