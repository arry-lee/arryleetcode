#二叉树的层次遍历
#2019-08-13 03:36:02

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        queue = [root]
        res = []
        
        while queue:
            tmp = []
            tmplen = len(queue)
            for i in range(tmplen):
                root = queue.pop(0)
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp)
        return res
