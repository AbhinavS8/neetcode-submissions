import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            
            
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(stones,x,y)

            diff = abs(x-y)
            if diff>0:
                heapq.heappush(stones,-diff)

        
        if len(stones)==1:
            return -stones[0]
        
        else:
            return 0