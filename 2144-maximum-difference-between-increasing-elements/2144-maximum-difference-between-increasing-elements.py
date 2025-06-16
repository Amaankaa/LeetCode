class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_ = -1

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                max_ = max(max_, nums[j] - nums[i])
        
        return max_ if max_ > 0 else -1