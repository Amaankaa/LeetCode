class Solution:
    def findMinArrowShots(self, nums: List[List[int]]) -> int:
        count = 1
        nums.sort(key = lambda x: x[1])
        end1 = nums[0][1]

        for i in range(1, len(nums)):
            starti = nums[i][0]
            if starti > end1:
                count += 1
                end1 = nums[i][1]

        return count 