# class Solution:
#     def isPalindrome(self, s: str) -> bool:
        
#         # start pointers on opposite sides, moving inwards
#         # if its not alphabet, skip
#         # check if theyre the same, then move both by one

#         l=0
#         s=s.lower()
#         r=len(s)-1

#         while l<r:
            
#             while not s[l].isalnum() and l<r:
#                 l+=1
            
#             while not s[r].isalnum() and l<r:
#                 r-=1
            
#             # print(s[l],s[r])
#             if s[l]!=s[r]:
#                 return False
#             l+=1
#             r-=1

#         return True
                
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))