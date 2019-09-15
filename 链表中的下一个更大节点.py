#链表中的下一个更大节点
#2019-08-11 09:37:03

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        inp = []
        out = [0]*10000
        counter = 0
        while head:   
            if not inp or head.val <= inp[-1][0]:
                inp.append((head.val,counter))
                head = head.next
                counter += 1
            else:
                _,c = inp.pop()
                out[c] = head.val

        return out[:counter]