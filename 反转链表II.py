#��ת����II
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

            # �ƶ��α굽 m ��
            while m>1:
                pre = pre.next
                cur = cur.next
                m-=1
                n-=1
        
            # ��¼
            con,tail = pre,cur  
            # ȫ�ַ�ת����
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