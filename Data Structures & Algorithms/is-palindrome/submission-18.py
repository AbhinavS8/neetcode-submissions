class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # start pointers on opposite sides, moving inwards
        # if its not alphabet, skip
        # check if theyre the same, then move both by one

        l=0
        
        r=len(s)-1

        while l<r:
            
            while not s[l].isalnum() and l<r:
                l+=1
            
            while not s[r].isalnum() and l<r:
                r-=1
            
            # print(s[l],s[r])
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1

        return True
                
            