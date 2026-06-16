from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=dict(Counter(nums))
        hashmap = sorted(hashmap.items(), key=lambda item: item[1])
        
        return [hashmap[i][0] for i in range(-1,-k-1,-1)]