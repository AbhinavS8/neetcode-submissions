class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        cost_ls=list()
        while len(prices)>=2:
            n=min(prices)
            for i in range(0,len(prices)):
                prices[i]=prices[i]-n
            pos=prices.index(0)

            cost_ls.append(max(prices[pos:]))

            for i in range(0,prices.count(0)):
                prices.remove(0)
        if (len(cost_ls)>0):
            return(max(cost_ls))
        else:
            return 0



# [9,0,4,5,6,0] - 6
# [9,4,5,6] 
# [5,0,1,2] - 2
# [5,1,2]
# [4,0,1] - 1
# [4,1]
# [3,0] - 0
