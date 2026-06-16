class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o_brackets=['{','[','(']
        c_brackets=['}',']',')']

        for i in s:
            if i in o_brackets:
                stack.append(i)
            elif i in c_brackets:
                if (len(stack)==0):
                    return False
                pos = c_brackets.index(i)
                if (o_brackets[pos]==stack[-1]):
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack)!=0:
            return False
        else:
            return True