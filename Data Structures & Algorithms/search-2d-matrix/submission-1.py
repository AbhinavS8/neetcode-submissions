class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(lis: List[int], target: int):
            
            l,r,m=0,len(lis),0
            if r==0:
                if lis[0]==target:
                    return 0
                else:
                    return -1

            while r-l>0:
                if len(lis[l:r])==1:
                    if lis[l]==target:
                        return l
                    else:
                        return -1
                m=(r-l)//2+l
                if target<lis[m]:
                    r=m
                elif target>lis[m]:
                    l=m
                elif target==lis[m]:
                    return m
            
            return -1
        v = binary_search([item for sublist in matrix for item in sublist],target)
        if v==-1:
            return False
        else:
            return True