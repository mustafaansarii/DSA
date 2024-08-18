# Problem URL: https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
class Solution:
    class Node:
        def __init__(self,data) -> None:
            self.next=None
            self.data=data

    def __init__(self) -> None:
        self.head=None

    def insert(self,value):
        new_node=self.Node(value)
        if self.head==None:
            head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def display(self):
        n=self.head
        if n:
            while n:
                print(n.data, end=' ')
                n=n.next
    def solve(self, *args, **kwargs):
        pass


if __name__=="__main__":
    obj=Solution()
    obj.insert(10)
    print(obj.display())
    