class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def canForm(diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        
        low, high = 0, nums[-1] - nums[0]
        res = high

        while low <= high:
            mid = (low + high)//2
            if canForm(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res