# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
        
#         # monotonic stack prolly
#         # [7:1]  max = 7
#         # [1:2] pop out 7, add to 1
#         # [7:1,1:2]
#         # [2:2, 1:2]
#         # [2:3, 1:2]
#         # [4:1, 2:3, 1:2]
#         # at end pop everything out and add
#         # do in reverse so can append easily

#         stack = []
#         mx = 0

#         def append_stack(height,val):
#             if len(stack)==0 or height>stack[-1][0]:
#                 stack.append([height,val])
            
#             elif height==stack[-1][0]:
#                 stack[-1][1]+=val
        
#         def pop_stack(height):
#             overk = 1
#             localmx = 0
#             while len(stack)>0 and height<stack[-1][0]:
#                 print(stack,i)

#                 cur = stack.pop(-1)
                
#                 localmx = max(localmx,cur[0]*cur[1])
#                 overk += cur[1]
            
#             append_stack(height,overk)
#             return localmx

#         for i in range(len(heights)):
            
#             if len(stack)==0 or heights[i]>=stack[-1][0]:

#                 append_stack(heights[i],1)
            
#             else:
#                 # pop logic
#                 mx = max(mx,pop_stack(heights[i]))
            
#             print(stack,i)

#         overk = 0
#         while len(stack)>0:
#             print(stack)
#             overk += stack[-1][0]
#             mx = max(mx,stack[-1][0]*overk)
#             stack.pop(-1)

#         return mx

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
