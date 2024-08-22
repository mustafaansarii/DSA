# Problem URL: https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1

class Solution1:
    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=temp
            temp=curr
        return prev

    def addOne(self,head):
        head=self.reverse(head)
        curr=head
        prev=None
        while curr and curr.data==9:
            curr.data=0
            prev=curr
            curr=curr.next
        if curr:
            curr.data+=1
        else:
            prev.next=Node(1)
        head=self.reverse(head)
        return head





