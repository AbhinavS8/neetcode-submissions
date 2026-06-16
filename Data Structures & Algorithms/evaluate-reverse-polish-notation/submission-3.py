class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        n1=n2=0

        for i in tokens:

            if i in ["+","-","*","/"]:
                n2=stack.pop()
                n1=stack.pop()
                stack.append(str(int(eval(n1+i+n2))))
            
            else:
                stack.append(i)
        
        return int(stack[0])