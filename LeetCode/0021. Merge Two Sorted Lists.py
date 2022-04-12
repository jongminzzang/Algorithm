# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1, t2 = list1, list2
        answer = ListNode(-101, None)
        answer_head = answer
        while t1 and t2:
            if t1.val < t2.val:
                answer.next = t1
                answer = answer.next
                t1 = t1.next
            else :
                answer.next = t2
                answer = answer.next
                t2 = t2.next
        
        answer.next = t1 if t1 else t2
        
        return answer_head.next
