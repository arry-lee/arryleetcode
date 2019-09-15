#对链表进行插入排序
#2019-08-11 19:22:44

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        
        # 断链
        sorted_head = head
        unsort_head = head.next
        sorted_head.next = None
        
        # 取头
        while unsort_head:
            to_sort = unsort_head
            unsort_head = unsort_head.next
            
            # 插入
            pre = dummy = ListNode(0)
            pre.next = sorted_head
            cur = sorted_head
            while cur and cur.val < to_sort.val:
                cur = cur.next
                pre = pre.next
            
            pre.next = to_sort
            to_sort.next = cur
            sorted_head = dummy.next
        return sorted_head
        