class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = []
        
        sorted_cnt = sorted(cnt.items(), key = lambda x: x[1], reverse=True)

        i = 0

        for key, value in sorted_cnt:
            if i < k:
                res.append(key)
            else: 
                break
            i += 1

        return res