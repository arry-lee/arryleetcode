#��������
#2019-08-11 06:57:51

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head # �ݹ��յ�
                
#         s, f = head, head.next
#         while f and f.next:
#             s, f = s.next, f.next.next      
#         mid, s.next= s.next, None          # ����ָ�����е�
               
#         l, r = self.sortList(head), self.sortList(mid)  # ��������
        
#         c = d = ListNode(0)
#         while l and r:
#             if l.val < r.val:
#                 c.next, l = l, l.next
#             else:
#                 c.next, r = r, r.next
#             c = c.next
              
#         c.next = l or r        
#         return d.next
 
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        rec=[]
        head1=head0=head
        while head0:
            rec.append(head0.val)
            head0=head0.next
        rec.sort()
        for i in rec:
            head1.val=i
            head1=head1.next
        return head            
            