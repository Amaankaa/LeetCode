class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(current):
            if len(current) == n:
                res.append(current)
                return
            
            dfs(current + '1')

            if not current or current[-1] == '1':
                dfs(current + '0')
            
        dfs('')
        return res
