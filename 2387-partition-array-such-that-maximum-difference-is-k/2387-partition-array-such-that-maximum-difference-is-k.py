class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        curr = nums[0]

        for i in range(len(nums)):
            if (nums[i] - curr) > k:
                count += 1
                curr = nums[i]
        
        return count