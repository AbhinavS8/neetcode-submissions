class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=''
        for i in s:
            if i.isalnum():
                news+=i.lower()
        if news==news[::-1] or len(s)==1:
            return True
        return False