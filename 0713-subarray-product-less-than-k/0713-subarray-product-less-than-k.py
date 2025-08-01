class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left, product, count = 0, 1, 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count