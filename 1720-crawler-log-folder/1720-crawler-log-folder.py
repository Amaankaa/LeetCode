class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []
        for log in logs:
            if log == "../" and res:
                res.pop()
            elif log == "./" or (log == "../" and not res):
                continue
            else:
                res.append('a')
        return len(res)