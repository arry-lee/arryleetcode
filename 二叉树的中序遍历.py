#二叉树的中序遍历
#2019-02-24 19:52:22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        if not root:
            return res
        
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        
        return res