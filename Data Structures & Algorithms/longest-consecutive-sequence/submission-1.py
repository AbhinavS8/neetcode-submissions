class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # longest c
        # first hash everything into a dict/set
        # check if n-1 exists, if it does ignore it
        # else iterate through until you reach the end and count the length

        st = set(nums)
        maxl = 0
        for i in st:
            
            if i-1 in st:
                continue
            else:
                curl = 1
                while True:
                    if i+1 in st:
                        curl+=1
                        i+=1
                    else:
                        break 
                
                maxl = max(maxl,curl)
        
        return maxl