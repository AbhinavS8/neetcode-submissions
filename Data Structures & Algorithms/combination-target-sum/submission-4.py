class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # start with smallest no.
        # 2 +5,2 +9 >
        # 2+2 +5, 2+2 +6
        # 2+2+2 +5
        # 2+2+2+2
        # 2+2+2+2+2
        # 5 +6
        # 5+5
        # 6 +9
        # 6+6
        # 9
        # Backtracking optimizations:
        # - Pass running sum (O(1) check) instead of recomputing sum().
        # - Reuse one path with append/pop; copy only when saving a result.
        # - Use indices to avoid duplicate permutations and unnecessary branching.
        final = []

        def backtrack(curpath):

            if sum(curpath)>target:
                return -1
            
            if sum(curpath)==target:
                final.append(curpath)
                return 1
            
            for i in nums:
                if len(curpath)!=0 and i<curpath[-1]:
                    continue
                curpath.append(i)
                backtrack(curpath.copy())
                curpath.remove(i)
        
        backtrack([])
        return final
                
        
            
            