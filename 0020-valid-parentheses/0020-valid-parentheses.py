class Solution:
    def isValid(self, s: str) -> bool:
        dict_ = {'(':')', '[':']', '{':'}'}
        stack = []

        for char in s:
            if char in dict_:
                stack.append(char)
            else:
                if not stack or dict_[stack.pop()] != char:
                    return False
        
        return not stack