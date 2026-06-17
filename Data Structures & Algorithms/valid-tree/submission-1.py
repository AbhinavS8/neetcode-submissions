class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # tree should not have cycles, thats it I think
        # undirected edges, so if connected itself, should count
        
        path = set()
        visited = set()

        adj_list = {i:[] for i in range(n)}

        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])

        def dfs(node, parent):
            
            visited.add(node)
            if node in path:
                return False
            
            path.add(node)

            for i in adj_list[node]:
                if i == parent:
                    continue

                if not dfs(i, node):
                    return False
            
            path.remove(node)
            return True

        
        if not dfs(0, None):
            return False
        
        if len(visited) != n:
            return False
        return True