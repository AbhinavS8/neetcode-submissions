class MedianFinder:

    def __init__(self):
        
        self.bottom = []
        self.top = []

        self.bn = 0
        self.tn = 0

    def addNum(self, num: int) -> None:
        
        if self.bn == 0:
            self.bn+=1
            self.bottom.append(-num)
            return
        
        if num > -self.bottom[0]:
            self.tn+=1
            heapq.heappush(self.top,num)
        
        else:
            self.bn+=1
            heapq.heappush(self.bottom,-num)
        
        # correction

        if self.bn - self.tn >= 2:
            # push from bottom to top
            temp = -heapq.heappop(self.bottom)
            heapq.heappush(self.top,temp)
            self.bn -= 1
            self.tn += 1

        elif self.tn - self.bn >= 2:
            temp = -heapq.heappop(self.top)
            heapq.heappush(self.bottom,temp)
            self.tn -= 1
            self.bn += 1


    def findMedian(self) -> float:
        
        if self.tn == self.bn == 0:
            return 0
        
        if (self.tn + self.bn)%2 == 0:
            return (self.top[0]-self.bottom[0])/2
        
        else:
            if self.tn > self.bn:
                return self.top[0]
            return -self.bottom[0]
        