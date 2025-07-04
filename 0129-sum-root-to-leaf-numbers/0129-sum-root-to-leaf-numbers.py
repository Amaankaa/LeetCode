# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, path):
            nonlocal res
            if not root:
                return
            
            path = path*10 + root.val
            if not root.left and not root.right:
                res += path
                return
            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, 0)
        return res