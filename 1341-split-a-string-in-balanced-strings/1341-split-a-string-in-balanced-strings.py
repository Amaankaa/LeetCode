class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        cnt = {'R':0, 'L':0}

        for char in s:
            cnt[char] += 1
            if cnt['R'] == cnt['L']:
                res += 1
        
        return res