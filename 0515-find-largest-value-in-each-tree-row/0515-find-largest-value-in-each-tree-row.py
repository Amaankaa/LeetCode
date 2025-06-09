# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            if not root:
                return 
            queue = deque([root])

            while queue:
                level_size = len(queue)
                currLevel = []

                for _ in range(level_size):
                    node = queue.popleft()
                    if node: currLevel.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

                res.append(max(currLevel))

        bfs(root)
        return res