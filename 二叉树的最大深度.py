#二叉树的最大深度
#2019-08-13 02:46:47

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return max(l,r)+1
        