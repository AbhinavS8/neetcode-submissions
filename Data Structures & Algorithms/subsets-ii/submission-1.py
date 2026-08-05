# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

#         # [1] and [1,2] should not repeat for [1,2,1]
#         # normally could recurse, adding or not adding each time

#         nums.sort()
#         visited = []
#         res = []


#         def backtrack(cur,index):
            
#             print(cur,index,visited)
#             if index==len(nums):
#                 res.append(cur)
#                 cur = []
#                 return
            
#             if cur == [] and nums[index] in visited:
#                 backtrack(cur,index+1)

#                 return

#             if cur==[] and nums[index] not in visited:
#                 visited.append(nums[index])
            
#             backtrack(cur+[nums[index]],index+1)


        
#         backtrack([],0)
#         return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, subset):
            res.append(subset[::])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res
