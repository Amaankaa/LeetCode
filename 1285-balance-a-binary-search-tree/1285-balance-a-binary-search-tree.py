# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        
        dfs(root)

        def helper(l, r):
            if l > r:
                return
            m = (l + r)//2
            root = TreeNode(arr[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        
        return helper(0, len(arr) - 1)