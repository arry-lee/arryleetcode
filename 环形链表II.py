#ª∑–Œ¡¥±ÌII
#2019-03-31 01:19:16

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        
        while slow and fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return None
            if slow is fast:
                break
        else:
            return None
        
        fast = head
        while True:
            if slow is fast:
                return slow
            slow = slow.next
            fast = fast.next
        