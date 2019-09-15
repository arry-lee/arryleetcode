#路径总和II
#2019-08-11 23:14:20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
                # 定义一列表用来保存所有路径
        paths = []

        def traverse(root, sum, path=[]):
            if root is None:
                return 
            if root.left is None and root.right is None:
                new_path = path+[root.val]
                if sum == root.val:
                    paths.append(path+[root.val])
            elif root.left is None:
                traverse(root.right, sum-root.val, path+[root.val])
            elif root.right is None:
                traverse(root.left, sum-root.val, path+[root.val])
            else:
                traverse(root.left, sum-root.val, path+[root.val])
                traverse(root.right, sum-root.val, path+[root.val])
        traverse(root, sum)
        return paths
                
        
        