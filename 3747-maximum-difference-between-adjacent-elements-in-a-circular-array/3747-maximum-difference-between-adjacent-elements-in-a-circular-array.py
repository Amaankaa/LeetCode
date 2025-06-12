class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(len(nums)):
            res = max(res, abs(nums[i] - nums[(i + 1)%n]))
        return res