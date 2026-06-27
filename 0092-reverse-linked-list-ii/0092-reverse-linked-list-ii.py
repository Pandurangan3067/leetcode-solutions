# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        l=[]
        while head is not None:
            l.append(head.val)
            head=head.next
        i,n=0,len(l)-1
        c=ListNode(0)
        d=c
        while i<left-1:
            d.next=ListNode(l[i])
            i+=1
            d=d.next
        i=right-1
        while i>=left-1:
            d.next= ListNode(l[i])
            i-=1
            d=d.next
        for j in l[right:]:
            print(j)
            d.next=ListNode(j)
            d=d.next
        return c.next

