# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        level = 0

        while q:
            size = len(q)
            level_nodes = []

            for _ in range(size):
                node = q.popleft()
                if node: level_nodes.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if level%2 == 1:
                level_nodes.reverse()
                res.append(level_nodes)
                level += 1
                continue
            res.append(level_nodes)
            level += 1
        
        return res