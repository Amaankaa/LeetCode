# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            level_nodes = []

            for i in range(size):
                node = q.popleft()
                level_nodes.append(node)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)

            if level%2 == 1:
                i, j = 0, len(level_nodes) - 1
                while i < j:
                    level_nodes[i].val, level_nodes[j].val = level_nodes[j].val ,  level_nodes[i].val
                    i += 1
                    j -= 1
            level += 1
        return root               
