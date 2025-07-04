class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and dict_[s[i]] < dict_[s[i + 1]]:
                res -= dict_[s[i]]
            else:
                res += dict_[s[i]]
        
        return res
        