# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         newstrs={}
#         #use tuple of characters so you can use as dictionary key
#         for st in strs:
#             dct = {}
#             for ch in st:
#                 dct[ch]=1
            
#             if dct in newstrs:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())