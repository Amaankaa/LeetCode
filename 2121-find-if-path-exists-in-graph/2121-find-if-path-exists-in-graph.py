class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        visited = set()

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)

                    if found:
                        return True
            return False
        
        return dfs(source, visited)