class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry=1
        for i in range(-1,-len(digits)-1,-1):
            
            print(i,digits[i])
            if carry and digits[i]==9:
                digits[i] = 0
                carry=1
            
            elif carry:
                digits[i]+=1
                carry=0
    
        
        if carry==1:
            digits=[1]+digits

        return digits
            