class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #optimized brute force/backtracking
        li=[]
        curr=[]
        l=r=0

        def backtracking(l,r):

            if l==r==n:
                li.append("".join(curr))
                return

            if l<n:
                curr.append("(")
                backtracking(l+1,r)
                curr.pop()

            if r<l:
                curr.append(")")
                backtracking(l,r+1)
                curr.pop()

        backtracking(0,0)
        return li