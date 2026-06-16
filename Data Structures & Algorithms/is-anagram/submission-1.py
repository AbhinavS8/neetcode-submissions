class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # hash both?
        # for fixed size, could use a character array

        w1 = [0,] *26
        w2 = w1.copy() # dEEP copy

        if len(s)!=len(t):
            return False
        
        for i in range(0,len(s)):
            l1 = ord(s[i])-ord("a")
            l2 = ord(t[i])-ord("a")

            w1[l1]+=1
            w2[l2]+=1

        if w1==w2:
            return True
        else:
            return False
