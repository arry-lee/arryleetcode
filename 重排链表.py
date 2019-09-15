#重排链表
#2019-03-31 02:25:16

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 边界判断
        if not head or not head.next or not head.next.next:
            return
        # 快慢指针找中点
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next

        # 打断链表
        l = s.next 
        s.next = None
        
        # 逆序链表
        n = l.next
        l.next = None
        while n:
            p = n.next
            n.next = l
            l = n
            n = p
        
        # 合并链表
        h = head
        while l:
            h1,l1 = h.next, l.next
            l.next = h1
            h.next = l
            h, l = h1, l1
            

        
        