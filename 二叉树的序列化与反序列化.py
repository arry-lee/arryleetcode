#二叉树的序列化与反序列化
#2019-07-25 20:09:31

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 层序遍历
        queue = [root]
        s = ""
        while queue:
            root = queue.pop(0)
            if root:
                s += str(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                s += "null"
            s += " "
        print(s)
        return s

            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split()
        print(tree)
        if tree[0] == "null":
            return None
        queue = []
        root = TreeNode(int(tree[0]))
        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if cur is None:
                continue
            cur.left = TreeNode(int(tree[i])) if tree[i] != "null" else None
            cur.right = TreeNode(int(tree[i+1])) if tree[i+1] != "null" else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))