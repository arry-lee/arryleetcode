#Ğı×ªÁ´±í
#2019-08-11 07:09:50

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dq = deque()
        
        head1=head0=head
        while head0:
            dq.append(head0.val)
            head0 = head0.next
        
        dq.rotate(k)
        
        while head1:
            head1.val=dq.popleft()
            head1=head1.next
        return head