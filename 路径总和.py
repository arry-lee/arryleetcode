#Â·¾¶×ÜºÍ
#2019-07-25 17:28:27

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        else:
            if not root.left and not root.right:
                return root.val == sum
            else:
                return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)