class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return new_node.data
        self.tail.next = new_node
        self.tail = new_node
        return new_node.data

    def dequeue(self):
        if self.head is None: return "Empty LL"
        a = self.head.data
        self.head = self.head.next
        return a

    def print(self):
        if self.head is None: return "Empty! LL"
        n = self.head
        while n:
            print(n.data, end=' ')
            n = n.next

    def size(self):
        if self.head is None: return 0
        count = 0
        n = self.head
        while n:
            n = n.next
            count += 1
        return count

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    Q = Queue()  # Create a new Queue object

    # Enqueue some elements
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)

    # Print the elements in the queue
    print("Queue elements:")
    Q.print()
    print()

    # Dequeue elements and print them
    print("Dequeuing elements:")
    print(Q.dequeue())  # Output: 10
    print(Q.dequeue())  # Output: 20
    print(Q.dequeue())  # Output: 30
    print(Q.dequeue())  # Output: Empty LL

    # Check if the queue is empty
    print("Is the queue empty?", Q.isEmpty())  # Output: True
