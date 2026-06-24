# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional:
        l=[]
        d=head
        while d is not None:
            l.append(d.val)
            d=d.next
        a=ListNode(0)
        b=a
        i,n=0,len(l)
        if n%2==0:
            while i<n:
                b.next=ListNode(l[i+1])
                b=b.next
                b.next=ListNode(l[i])
                b=b.next
                i+=2
        else:
            while i<n-1:
                b.next=ListNode(l[i+1])
                b=b.next
                b.next=ListNode(l[i])
                b=b.next
                i+=2
            b.next=ListNode(l[i])
        return a.next


            
             