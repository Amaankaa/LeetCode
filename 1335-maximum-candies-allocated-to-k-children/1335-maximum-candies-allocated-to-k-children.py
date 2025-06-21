class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        ans = 1

        left, right = 1, sum(candies)//k

        while left <= right:
            mid = (left + right)//2
            count = 0
            for candy in candies:
                count += candy//mid
            
            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans