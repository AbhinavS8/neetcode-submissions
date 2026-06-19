class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = []
        for i in range(n+1):
            
            cnt = 0
            for j in range(32):
                cnt += i & 1
                i = i >> 1
            
            output.append(cnt)
        
        return output