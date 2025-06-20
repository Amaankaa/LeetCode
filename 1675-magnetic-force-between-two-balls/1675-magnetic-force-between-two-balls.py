class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = -1
        left, right = 0, position[-1] - position[0]
        
        while left <= right:
            mid = (left + right)//2
            if self.isOkay(mid, position, m):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def isOkay(self, mid, position, m):
        prevIdx = 0
        count = 1

        for i in range(1, len(position)):
            if ((position[i] - position[prevIdx]) >= mid):
                prevIdx = i
                count += 1
        
        return count >= m

