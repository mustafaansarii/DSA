# https://leetcode.com/problems/reverse-linked-list/description/

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLL:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def _print(self):
        if self.head is None: return "Sll is Empty!"
        n=self.head

        while n is not None:
            print(n.data, end=' ')
            n=n.next

    def Reverse(self):
        if self.head is None: return "Sll is Empty!"
        if self.head.next is None: return self.head
        n=self.head
        s=[]
        while n:
            s.append(n.data)
            n=n.next
        k=s[::-1]
        print(k)

if __name__ == '__main__':
    s=SinglyLL()
    s.insert_begin(1)
    s.insert_begin(11)
    s.insert_begin(12)
    s._print()
    s.Reverse()
