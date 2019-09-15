#�������ĺ������
#2019-02-24 20:45:44

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
#         """�ݹ鷨"""
#         res = []
#         def postorder(root):
#             if root:
#                 postorder(root.left)
#                 postorder(root.right)
#                 res.append(root.val)
        
#         postorder(root)
#         return res        

        """������"""

        if root is None:
            return []

        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]