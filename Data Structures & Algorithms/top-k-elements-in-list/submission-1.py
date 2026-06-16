from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=dict(Counter(nums))
        n=len(nums)
        # hashmap = sorted(hashmap.items(), key=lambda item: item[1])
        linked_hash = [[] for i in range(n)]

        for i in hashmap:
            linked_hash[hashmap[i]-1].append(i)

        ans=[]
        while len(ans)<k:
            ans+=linked_hash.pop() 
        
        return ans
        # return [hashmap[i][0] for i in range(-1,-k-1,-1)]

