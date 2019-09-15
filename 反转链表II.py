#反转链表II
#2019-08-11 08:13:59

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        
        if m > 1:
            pre = ListNode(0)
            pre.next = head

            # 移动游标到 m 处
            while m>1:
                pre = pre.next
                cur = cur.next
                m-=1
                n-=1
        
            # 记录
            con,tail = pre,cur  
            # 全局翻转链表
            pre = None
            while n>0:
                cur.next, pre, cur = pre, cur, cur.next
                n-=1
            con.next = pre
            tail.next = cur
            return head
        
        else:
            pre = None
            while n>0:
                cur.next, pre, cur = pre, cur, cur.next
                n-=1
            
            head.next = cur
            return pre