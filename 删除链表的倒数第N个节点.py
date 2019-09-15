#删除链表的倒数第N个节点
#2019-08-13 02:43:55

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next: return None
        
        dummy = prev = ListNode(0)
        prev.next = head
        slow = head
        fast = head
        
        while n>0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
            prev = prev.next
        
        prev.next = slow.next
        return dummy.next
            