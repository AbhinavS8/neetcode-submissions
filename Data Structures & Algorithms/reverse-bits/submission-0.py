class Solution:
    def reverseBits(self, n: int) -> int:
        
        new = 0
        for i in range(31):

            if n & 1:
                new = new | 1
            
            n = n >> 1
            new = new << 1
        
        if n & 1:
            new = new | 1
            
        return new
