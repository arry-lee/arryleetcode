#��ת����
#2019-08-13 02:16:59

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:     
        p = None
        c = head     
        while c:# ʹ��python�Ľ������Ͳ��ÿ��Ǹ�ֵ˳����
            c.next,c,p = p,c.next,c       
        return p
    
        # �ݹ�Ļ���������
#         if not head or not head.next:
#             return head
        
#         p = self.reverseList(head.next)
#         q = p
#         while q.next:
#             q = q.next
#         q.next = head
#         head.next = None
#         return p

            
        
            