class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        average_count = 0
        
        def dfs(node):
            nonlocal average_count
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            cur_avg = total_sum // total_count

            if cur_avg == node.val:
                average_count += 1
            
            return (total_sum, total_count)
        
        dfs(root)
        return average_count
