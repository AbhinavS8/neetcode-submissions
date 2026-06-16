# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         s=""
#         for st in strs:
#             s+=st+"\0"
        
#         return s

#     def decode(self, s: str) -> List[str]:
#         if s=="\0":
#             return [""]
#         return s.split("\0")[:-1]

class Solution:
    spacesArr=[]

    def encode(self, strs: List[str]) -> str:
        self.spacesArr.clear()
        l=len(strs)
        ans=""

        if l==0:
            return "\0"
        elif l==1:
            return strs.pop()
        else:
            for i in range(0,l-1):
                ans+=strs[0]
                self.spacesArr+=[len(strs[0])]
                strs.pop(0)
            else:
                ans+=strs[0]
        return ans


    def decode(self, s: str) -> List[str]:
        ls=[]
        ptr=0

        if s=="\0":
            return []
        if s=="":
            return [""]
        for i in self.spacesArr:
            print(ptr)
            ls+=[s[ptr:ptr+i]]
            ptr+=i
        ls+=[s[ptr:]]
        
        return ls