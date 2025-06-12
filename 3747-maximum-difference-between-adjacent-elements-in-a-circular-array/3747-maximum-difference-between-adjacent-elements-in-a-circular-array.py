class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = float('-inf')

        for i in range(len(nums)):
            adj = (i + 1)%len(nums)
            calculated = abs(nums[i] - nums[adj])
            res = max(res, calculated)
        return res