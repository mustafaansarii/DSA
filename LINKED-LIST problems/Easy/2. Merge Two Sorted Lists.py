# https://leetcode.com/problems/merge-two-sorted-lists/description/
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Sll:
    def __init__(self):
        self.head=None
    def add_begin(self,x):
        new_node=Node(x)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def _print(self):
        if self.head is None: return "Sll is Empty!"
        n=self.head
        while n.next.next is not None:
            print(n.data, end=' ')
            n=n.next
if __name__ == '__main__':



