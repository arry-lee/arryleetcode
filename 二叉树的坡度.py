#¶þ²æÊ÷µÄÆÂ¶È
#2019-01-09 22:09:21

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
        
            if not root:
                return 0,0
            
            ldif,lsum = traverse(root.left)
            rdif,rsum = traverse(root.right)
            return abs(lsum-rsum) + ldif + rdif, lsum+rsum+root.val  
        
        d,s = traverse(root)
        return d
    
