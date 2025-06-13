class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minUnfairness = float('inf')
        children = [0] * k

        def backtrack(i):
            if i == len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(children))
                return
            
            for j in range(k):
                children[j] += cookies[i]
                
                # \U0001f525 Prune if already worse
                if children[j] < self.minUnfairness:
                    backtrack(i + 1)
                
                children[j] -= cookies[i]

                # \U0001f9e0 Optimization: if this kid was empty before, no need to give same to another empty kid
                if children[j] == 0:
                    break

        cookies.sort(reverse=True)  # \U0001f448 Helps prune earlier
        backtrack(0)
        return self.minUnfairness
