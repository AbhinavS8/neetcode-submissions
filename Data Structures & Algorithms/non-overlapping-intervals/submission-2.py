# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
#         # can use greedy approach

#         intervals.sort(key = lambda x:x[0])

#         prevend = -1
#         removecnt = 0

#         for i in intervals:

#             if prevend == -1:
#                     prevend = i[1]

            
#             elif prevend > i[0]:
#                 removecnt+=1
                
#                 prevend = min(i[1],prevend)
            
#             if prevend <= i[0]:
#                 prevend = i[1]

#         return removecnt

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res