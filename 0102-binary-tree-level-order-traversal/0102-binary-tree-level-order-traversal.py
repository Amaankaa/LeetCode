# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):
            if not root:
                return []
            levels = []
            queue = deque([node])

            while queue:
                level_size = len(queue)
                currLevel = []

                for _ in range(level_size):
                    curr = queue.popleft()
                    currLevel.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                
                levels.append(currLevel)
            
            return levels

        
        return bfs(root)
