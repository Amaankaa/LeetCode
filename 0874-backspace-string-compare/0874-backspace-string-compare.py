class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_char(s, index):
            backspace_count = 0
            while index >= 0:
                if s[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index
        
        i, j = len(s)-1, len(t)-1
        while i >= 0 or j >= 0:
            i = next_valid_char(s, i)
            j = next_valid_char(t, j)
            
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
        
        return True
