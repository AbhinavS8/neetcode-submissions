# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
#         # start with center of the palindrome
#         # maxp = 0
#         # maxstr = ""

#         # lens = len(s)
#         # if lens == 1:
#         #     return s
        
#         # if lens == 2:
#         #     if s[0]==s[1]:
#         #         return s
#         #     else:
#         #         return s[0]
        
#         # if lens == 3:
#         #     if s[0]==s[2]:
#         #         return s
            
#         #     if s[0]==s[1]:
#         #         return s[:2]
            
#         #     if s[1]==s[2]:
#         #         return s[1:]
            
#         #     return s[0]

#         # for i in range(lens):
#         #     cur = 0
#         #     l,r = i,i
#         #     st = ""
#         #     if l-1>=0:
#         #         if s[i]==s[l-1]:
#         #             cur+=1
#         #             l-=1
#         #             st = s[l+1:r]

#         #     while l>=0 and r<lens:

#         #         if s[l]==s[r]:
#         #             st = s[l:r+1]
#         #             cur+=2
#         #             l-=1
#         #             r+=1
#         #         else:
#         #             break
            
#         #     print(st)

#         #     if cur>maxp:
#         #         maxp = cur
#         #         maxstr = st

#         # print(maxp)
#         # return maxstr

#         # try to fit it into a recurseive format

#         # [a,b,a] [b]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]