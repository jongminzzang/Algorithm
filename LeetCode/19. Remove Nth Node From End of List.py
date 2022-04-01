# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
    
        return l[((len(l))//2)]
