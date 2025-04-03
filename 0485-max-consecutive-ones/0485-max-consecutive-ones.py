class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window = []
        max_len = 0

        left = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                window.append(nums[right])
                max_len = max(max_len, len(window))
            else:
                window = []
        
        return max_len
