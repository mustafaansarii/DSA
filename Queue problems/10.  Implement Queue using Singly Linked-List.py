class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def Enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def _print(self):
        if self.head is None:
            return "Queue is Empty!"
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next
            print()

    def Dequeue(self):
        if self.head is None:
            return "Queue is Empty!"
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next


if __name__ == '__main__':
    Q = Queue()

    Q.Enqueue(10)
    Q.Enqueue(20)
    Q.Enqueue(30)


    Q.Dequeue()



    print(Q._print())


