class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_i = max_i = bad_i = -1

        for i, n in enumerate(nums):
            if n > maxK or n < minK:
                bad_i = i
            
            if n == minK:
                min_i = i
            if n == maxK:
                max_i = i
            
            res += max(0, min(min_i, max_i) - bad_i)
        return res

        
                