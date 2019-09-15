#从前序与中序遍历序列构造二叉树
#2019-08-11 21:55:12

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        # 根
        root = TreeNode(preorder[0])
        # 切割
        root_index_inorder = inorder.index(preorder[0])
        leftinorder = inorder[:root_index_inorder]
        rightinorder = inorder[root_index_inorder+1:]
        leftpreorder = preorder[1:root_index_inorder+1]
        rightpreorder = preorder[root_index_inorder+1:]
        # 递归的建左子树右子树
        root.left = self.buildTree(leftpreorder,leftinorder)
        root.right = self.buildTree(rightpreorder,rightinorder)
        
        return root