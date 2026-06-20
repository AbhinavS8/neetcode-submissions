class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        # just create a new array, easier that way
        newstart = newInterval[0]
        newend = newInterval[1]
        res = []
        flag = True

        for i in intervals:
            print(i,newstart,newend)
            if i[1] < newstart:
                res.append(i)
                continue
            
            if i[0] > newend:
                if flag:
                    res.append([newstart,newend])
                
                flag = False
                res.append(i)

            if i[1] >= newstart:
                newstart=min(newstart,i[0])
                newend = max(newend,i[1])
                
            if i[0] <= newend:
                newstart=min(newstart,i[0])
                newend = max(newend,i[1])

        if flag:
            res.append([newstart,newend]) 
        return res            
            











        # newstart = newInterval[0]
        # newend = newInterval[1]

        # for i in range(0,len(intervals)):
            
        #     inval = intervals[i]

        #     if inval[1] < newstart:
        #         continue
            
        #     if newstart < inval[1]:
        #         newstart = inval[0]
        #         inval[1]=max(newend,inval[1])
        #         intervals[i]=inval
        #         continue

        #     if inval[0] > newend:
        #         intervals.insert(i,newInterval)
        #         return intervals
            
        #     if inval[0] < newend:
        #         inval[0] = newstart
        #         intervals[i]=inval
                
        #         return intervals
            
        # return intervals

                    

        # for i in intervals:

        #     if i[1] < newInterval[0]:
        #         continue
            
        #     if i[0] > newInterval[1]: