# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

# Definition for singly-linked list.
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
        self.head=None

    def insert(self,x):
        new_node=ListNode(x)
        new_node.next=self.head
        self.head=new_node

    def print(self):
        if self.head is not None:
            n=self.head
            while n:
                
                print(n.val,end=' ')
                n=n.next

    def clear(self):
        self.head=None

    def doubleIt(self):
        list=[]
        n=self.head
        while n:
            list.append(n.val)
            n=n.next
        self.clear()
        result = [int(''.join(map(str, list)))]
        for i in result:
            a = i * 2
        result1 = [int(digit) for digit in str(a)]
        reult1=result1[::-1]
        for i in result1:
            self.insert(i)
        return self.print()
      



s=Solution()
      

        
if __name__ == '__main__':
    s=Solution()
    s.insert(3)
    s.insert(2)
    s.insert(1)
    print()
    s.print()
    s.doubleIt()
    s.print



 