#��������
#2019-08-13 02:17:40

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #  O(n) ʱ�临�ӶȺ� O(1) �ռ临�Ӷ�
        # һ�α���
        #
        # ����ָ�뵽�м�
        # reverse ֮��һ��
        
        # �ݹ�
        
        # ������û��ϵ ������ֵ
        
        if not head or not head.next:return True
        
        def generator(head):
            while head:
                yield head.val
                head = head.next
        
        
        x = list(generator(head))
        y = list(reversed(x))
        print(x,y)
        
        return x==y
        