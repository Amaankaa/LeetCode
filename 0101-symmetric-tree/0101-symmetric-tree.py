# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return True
            queue = deque([root])

            while queue:
                level_size = len(queue)
                currLevel = []

                for _ in range(level_size):
                    node = queue.popleft()
                    if node is None:
                        currLevel.append(None)
                        continue
                    currLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

                if currLevel != currLevel[::-1]:
                    return False
            return True

        return bfs(root)

                