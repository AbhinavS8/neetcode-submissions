class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if no day after keep it as 0
        # [30,38,30,36,35,40,28] pop 28
        
        res=[0]*len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while len(stack)!=0 and t>stack[-1][0]:
                st,si=stack.pop()
                res[si]=i-si
            stack.append((t,i))
        return res


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []  # pair: [temp, index]

#         for i, t in enumerate(temperatures):
#             while stack and t > stack[-1][0]:
#                 stackT, stackInd = stack.pop()
#                 res[stackInd] = i - stackInd
#             stack.append((t, i))
#         return res

