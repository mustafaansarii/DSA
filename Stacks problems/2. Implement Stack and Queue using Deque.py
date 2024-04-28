# https://www.geeksforgeeks.org/implement-stack-queue-using-deque/

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        self.prev=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def Enqueue(self,data):
        new_node=Node(data)
        if self.head is None: return "Queue is Empty!"
        if self.head.next is None:
            self.head=new_node
            new_node.prev=new_node
            new_node.next=new_node
            return
        self.head.prev.next=new_node
        new_node.prev=self.head.prev
        new_node.next=self.head
        self.head=new_node
    def _print(self):
        if self.head is None: return "Queue is Empty!"
        n=self.head
        while n is not n.next:
            print(n.data, end=' ')
            n=n.next
Q=Queue()
print(Q._print())
