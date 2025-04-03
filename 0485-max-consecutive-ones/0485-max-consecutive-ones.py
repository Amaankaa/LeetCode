class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window = []
        counter = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                counter += 1
                max_len = max(max_len, counter)
            else:
                counter = 0
        
        return max_len
