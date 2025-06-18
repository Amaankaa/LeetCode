class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []

        nums.sort()
        for i in range(0, len(nums), 3):
            res.append(nums[i:i+3])
        
        for arr in res:
            min_so_far = arr[0]
            max_diff = -1

            for num in arr:
                if num < min_so_far:
                    min_so_far = num
                else:
                    max_diff = max(max_diff, num-min_so_far)
            if max_diff > k:
                return []

        return res