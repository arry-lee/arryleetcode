#¶Ô³Æ¶þ²æÊ÷
#2019-08-13 03:10:28

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetic(left,right):
            if not left and not right:
                return True
            elif not left:
                return False
            elif not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return symmetic(left.left,right.right) and symmetic(left.right,right.left)
            
            
        if not root:return True
        return symmetic(root.left,root.right)