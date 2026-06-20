class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        pstart = -1
        pend = -1

        intervals.sort(key = lambda x:x[0])

        for i in intervals:

            if pstart == -1:
                pstart = i[0]
                pend = i[1]
                continue
            
            if i[0] > pend:
                res.append([pstart,pend])
                pstart = i[0]
                pend = i[1]
            
            if i[0] <= pend:
                pend = max(pend,i[1])
            
        if len(res) == 0 or res[-1]!=[pstart,pend]:
            res.append([pstart,pend])
        print(res)
        return res