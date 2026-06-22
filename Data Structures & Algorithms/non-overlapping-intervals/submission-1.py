class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # can use greedy approach

        intervals.sort(key = lambda x:x[0])

        prevend = -1
        removecnt = 0

        for i in intervals:

            if prevend == -1:
                    prevend = i[1]

            
            elif prevend > i[0]:
                removecnt+=1
                
                prevend = min(i[1],prevend)
            
            if prevend <= i[0]:
                prevend = i[1]
                
        return removecnt
