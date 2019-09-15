#分隔链表
#2019-08-11 04:18:51

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:        
        ld = lt = ListNode(0)
        gd = gt = ListNode(0)
        
        p = head
        
        while p:
            if p.val < x:
                lt.next = p
                lt = lt.next
            else:
                gt.next = p
                gt = gt.next
            p = p.next
            
        lt.next = gd.next
        gt.next = None # 最后一定要有None不然就是一个野指针
        
        ld = ld.next
        
        return ld