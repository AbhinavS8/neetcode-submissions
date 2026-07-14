import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i in nums:

            if len(heap)<k:

                heapq.heappush(heap,i)
                continue
            
            else:

                if heap[0] < i:

                    heapq.heappop(heap)
                    heapq.heappush(heap,i)

            # print(heap,nums)
        
        return heap[0]