#·­×ª¶þ²æÊ÷
#2019-03-31 10:14:28

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node:
                if node.left or node.right:
                    node.left, node.right = node.right, node.left
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return root