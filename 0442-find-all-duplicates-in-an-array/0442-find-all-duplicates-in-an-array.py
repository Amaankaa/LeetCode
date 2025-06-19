class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = {}
        res = []
        
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        for key, val in cnt.items():
            if val == 2:
                res.append(key)
        
        return res