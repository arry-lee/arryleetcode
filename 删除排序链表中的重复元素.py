#删除排序链表中的重复元素
#2019-08-11 03:51:29

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        p1,p2 = head,head.next
        
        while p2:
            if p1.val == p2.val:
                p2 = p2.next
                p1.next = p2
            else:
                p1 = p1.next
                p2 = p2.next
        return head