class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = [-1] * (n + 1)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node):
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 1 - color[node]

                    if not dfs(nei):
                        return False

                elif color[nei] == color[node]:
                    return False
            
            return True
        
        for n in range(1, n + 1):
            if color[n] == -1:
                if not dfs(n):
                    return False
        
        return True

