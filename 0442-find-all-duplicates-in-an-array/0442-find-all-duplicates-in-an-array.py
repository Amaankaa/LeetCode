class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        
        for key, val in cnt.items():
            if val == 2:
                res.append(key)
        
        return res