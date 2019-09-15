#�ཻ����
#2019-03-30 23:37:38

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        # �ж��ĸ��Ƚ϶�
        while pA and pB:
            pA = pA.next
            pB = pB.next
        
        # һ����
        if not pA and not pB:
            pshort = headA
            plong = headB
            
        elif not pA and pB:
            pshort = headA
            plong = headB
            while pB and plong:
                pB = pB.next
                plong = plong.next    
        else:
            pshort = headB
            plong = headA
            while pA and plong:
                pA = pA.next
                plong = plong.next
                
        while pshort and pshort is not plong:
            pshort = pshort.next
            plong = plong.next
        return pshort