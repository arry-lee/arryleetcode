#二叉树的层次遍历II
#2019-07-25 17:00:12

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # do something
        if not root:
            return []
        stack = [root]
        res = []
        
        while len(stack) != 0:
            tmp = []
            res_each = []
            for i in stack:
                res_each.append(i.val)
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            
            stack = tmp
            res.insert(0,res_each)
            
        return res
            
            