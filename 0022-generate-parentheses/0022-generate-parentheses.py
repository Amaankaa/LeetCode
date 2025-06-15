class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtrack(openedC, closedC):
            if openedC == closedC == n:
                res.append("".join(stack))
                return
            
            if openedC < n:
                stack.append("(")
                backtrack(openedC + 1, closedC)
                stack.pop()
            
            if closedC < openedC:
                stack.append(")")
                backtrack(openedC, closedC + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res