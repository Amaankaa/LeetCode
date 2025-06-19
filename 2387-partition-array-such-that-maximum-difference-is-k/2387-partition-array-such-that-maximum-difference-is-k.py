class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        curr = nums[0]
        n = len(nums)

        for i in range(n):
            if (nums[i] - curr) > k:
                count += 1
                curr = nums[i]
        
        return count