# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         res = set()

#         # have to find all solutions
#         temp = []
#         candidates.sort()

#         def recurse(index):
#             # print(temp, res)
            
            
#             if sum(temp) == target:
#                 res.add(tuple(temp))
#                 return
            
#             if sum(temp) > target:
#                 return

#             if index >= len(candidates):
#                 return

#             temp.append(candidates[index])
#             recurse(index+1)
#             temp.pop()
#             recurse(index+1)

#         recurse(0)
#         return [list(i) for i in res]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()


            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res