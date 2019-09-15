#��������ǰ�����
#2019-02-24 20:31:07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        """�ݹ鷨"""
#         res = []
#         def preorder(root):
#             if root:
#                 res.append(root.val)
#                 preorder(root.left)
#                 preorder(root.right)
        
#         preorder(root)
#         return res

        """������"""


        stack, res = [], []
        node = root
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right        
        return res
                