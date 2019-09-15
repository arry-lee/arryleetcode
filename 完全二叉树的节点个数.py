#完全二叉树的节点个数
#2019-08-11 21:41:48

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1