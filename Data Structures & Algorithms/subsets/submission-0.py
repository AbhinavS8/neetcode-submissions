class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        
        def recurse(curset,i):

            if i == len(nums):
                subsets.append(curset)
                return
            
            # print(subsets,curset,i)
            recurse(curset+[nums[i]],i+1)
            

            recurse(curset,i+1)


        # for i in range(nums):

        #     temp = []

        recurse(list(),0)

        return subsets
