class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ = Counter(s1)
        k = len(s1)

        window = Counter(s2[:k])

        if window == s1_:
            return True
        
        left = 0

        for right in range(k, len(s2)):
            window[s2[right]] += 1
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]
            
            if window == s1_:
                return True
            
            left += 1
        
        return False
