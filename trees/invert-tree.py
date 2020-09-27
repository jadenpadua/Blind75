# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while len(q):
            curr = q.pop(0)
            if curr is None:
                continue
            curr.left,curr.right = curr.right,curr.left
            q.append(curr.left)
            q.append(curr.right)
        return root
#
