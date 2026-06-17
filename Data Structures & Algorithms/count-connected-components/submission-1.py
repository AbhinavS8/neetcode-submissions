class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {i:[] for i in range(n)}

        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])

        visited = set()

        def dfs(node,parent):

            if node in visited and parent==None:
                return False
            
            if node in visited:
                return True
                
            visited.add(node)

            for i in adj_list[node]:
                if i==parent:
                    continue

                if not dfs(i,node):
                    return True

            return True
        
        i=0
        cnt=0
        while len(visited)<n:
            if dfs(i,None):
                cnt+=1
            i+=1
        
        return cnt