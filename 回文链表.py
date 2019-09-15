#回文链表
#2019-08-13 02:17:40

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #  O(n) 时间复杂度和 O(1) 空间复杂度
        # 一次遍历
        #
        # 快慢指针到中间
        # reverse 之后一样
        
        # 递归
        
        # 和链表没关系 看的是值
        
        if not head or not head.next:return True
        
        def generator(head):
            while head:
                yield head.val
                head = head.next
        
        
        x = list(generator(head))
        y = list(reversed(x))
        print(x,y)
        
        return x==y
        