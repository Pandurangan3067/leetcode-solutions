# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        l,n=[],0
        while head is not None:
            l.append(head.val)
            n+=1
            head=head.next
        l.sort()
        d=ListNode(l[0])
        c,i=d,1

        while i<n:
            c.next=ListNode(l[i])
            i+=1
            c=c.next
        return d
