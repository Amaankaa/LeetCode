class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min
            
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            left = dfs(node.left, curr_min, curr_max)
            right = dfs(node.right, curr_min, curr_max)

            return max(left, right)
        
        return dfs(root, root.val, root.val)