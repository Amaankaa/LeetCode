class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        length = 0

        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        
        if left == len(nums) - 1:
            return length
        
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        max_value = max(nums[left:right + 1])
        min_value = min(nums[left: right + 1])

        while left > 0 and nums[left - 1] > min_value:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < max_value:
            right += 1
        
        return right - left + 1
        
