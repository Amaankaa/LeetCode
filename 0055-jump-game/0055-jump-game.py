class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True