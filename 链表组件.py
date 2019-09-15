#链表组件
#2019-08-11 08:56:48

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [0 1 2 3 4]
# [0 1 2 0 4]
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        # 把G转换为布尔列表
#         Gb = [0]*10000
#         for x in G:
#             Gb[x] = True
        
        G=set(G)
        counter = 0
        while True:
            if head.val not in G:
                while head and head.val not in G:
                    head = head.next
            
            else:
                counter += 1
                while head and head.val in G:
                    head = head.next

            if not head:
                return counter
        
                    