class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Use a stack to keep track of scores at each depth
        
        for char in s:
            if char == '(':
                stack.append(0)  # Start with score 0 for a new depth level
            else:  # ')'
                val = stack.pop()
                if val == 0:  # Empty pair case: ()
                    stack[-1] += 1
                else:  # Non-empty pair case: (A)
                    stack[-1] += 2 * val
        
        return stack[0]