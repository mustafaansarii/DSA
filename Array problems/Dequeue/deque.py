class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:  # Deque is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, value):
        new_node = Node(value)
        if self.head is None:  # Deque is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")

        value = self.tail.value
        if self.head == self.tail:  # Only one element in the deque
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return value

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")

        value = self.head.value
        if self.head == self.tail:  # Only one element in the deque
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.tail.value

    def peekleft(self):
        if self.is_empty():
            return None
        return self.head.value

    def __len__(self):
        return self.size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return "Deque: " + " <-> ".join(map(str, elements))


# Example usage
if __name__ == "__main__":
    deque = Deque()

    deque.append(10)
    deque.append(20)
    deque.appendleft(5)
    deque.appendleft(1)

    print(deque)  # Deque: 1 <-> 5 <-> 10 <-> 20

    print(deque.pop())  # 20
    print(deque.popleft())  # 1

    print(deque)  # Deque: 5 <-> 10

    deque.append(30)
    deque.appendleft(2)

    print(deque)  # Deque: 2 <-> 5 <-> 10 <-> 30
    print("Peek:", deque.peek())  # Peek: 30
    print("Peek Left:", deque.peekleft())  # Peek Left: 2
