class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window ahhhh
        #abcca
        l=r=0

        max_sb=0
        hashset={}
        if len(s)==0:
            return 0

        if len(s)==1:
            return 1

        for i in s:
            if i in hashset:
                max_sb=max(max_sb,r-l)
                l = max(l, hashset[i] + 1)
        
            hashset[i]=r
            r+=1
            print(i,hashset,l,r,max_sb)

        max_sb=max(max_sb,r-l)

        return max_sb