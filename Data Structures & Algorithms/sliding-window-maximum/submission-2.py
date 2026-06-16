import heapq
from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #use maxheap
        #maintain hash
        #while finding max, check hash, if its not there pop
        #and find next max

        length=len(nums)

        if length==k:
            return [max(nums)]
        
        if k==1:
            return nums

        res=[]
        l=0
        r=k
        hashset=Counter(nums[l:r])
        mxheap=[-i for i in nums[l:r]]
        heapq.heapify(mxheap)
        res.append(-mxheap[0])

        while r<length:
            print(mxheap,hashset)
            hashset[nums[l]]-=1

            while hashset.get(-mxheap[0],0)<=0:
                heapq.heappop(mxheap)
                heapq.heapify(mxheap)
            

            mxheap.append(-nums[r])
            heapq.heapify(mxheap)
            print(l,r)
            hashset[nums[r]] = hashset.get(nums[r], 0) + 1

            l+=1
            r+=1

            res.append(-mxheap[0])

        
        return res
