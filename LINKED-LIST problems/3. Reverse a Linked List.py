# https://www.geeksforgeeks.org/reverse-a-linked-list/

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head= None

    def push(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def _print(self):
        if self.head is None: return "LL Empty!"
        n=self.head
        while n is not None:
            print(n.data, end=' ')
            n=n.next

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

        # new_list = None
        # current = head
        #
        # while current:
        #     next_node = current.next
        #     current.next = new_list
        #     new_list = current
        #     current = next_node
        #
        # return new_list


if __name__ == '__main__':
    S=Sll()
    S.push(12)
    S.push(13)
    S.push(12)
    S.push(15)
    S._print()
    print()
    S.Reverse()
    S._print()