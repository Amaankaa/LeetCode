class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append(i)
        
        return res