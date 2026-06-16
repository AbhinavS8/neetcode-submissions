from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #O(n) time and O(1) space?

        cnts1=Counter(s1)
        crr={}

        l=0
        cnts2={}
        for r in range(len(s1),len(s2)+1):
            print(l,r)
            cnts2=Counter(s2[l:r])

            if cnts2==cnts1:
                return True
            else:
                l+=1
        
        return False