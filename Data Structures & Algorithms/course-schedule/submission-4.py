class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # topological sort?
        # how to find first elements?
        # make a graph to store everything?
        # no cycles i guess

        # first make a graph with n nodes
        # iterate through prerequisites?
        # [0,1] 1->0 directed 
        
        #DFS 
        def dfs(course):
            # what does dfs do??
            # checks if its cycling
            # 
            # print(course,path)
            if course in path:
                return False
            
            path.add(course)

            if course in reqs:
                for req_course in reqs[course]:
                    if not dfs(req_course):
                        return False
                
                reqs[course]=[]
            
            path.remove(course)
            return True

        reqs = {}
        path = set()

        for i in prerequisites:
            if i[0] in reqs:
                reqs[i[0]].append(i[1])
            else:
                reqs[i[0]] = [i[1]]
        
        # print(reqs)
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        



