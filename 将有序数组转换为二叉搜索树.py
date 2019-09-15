#将有序数组转换为二叉搜索树
#2019-08-13 03:43:20

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        len_nums = len(nums)
        if len_nums == 0:return None
        if len_nums == 1:return TreeNode(nums[0])
        
        mid = len_nums//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
