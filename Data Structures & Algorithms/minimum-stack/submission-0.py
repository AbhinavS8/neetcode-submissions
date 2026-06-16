class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]
        self.cmin_index=0
        self.l=-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.l+=1
        if val<self.stack[self.cmin_index]:
            self.mins.append(self.cmin_index)
            self.cmin_index=self.l
        else:
            self.mins.append(-1)

    def pop(self) -> None:
        if self.mins[self.l]!=-1:
            self.cmin_index=self.mins[self.l]
        self.mins.pop()
        self.stack.pop()
        self.l-=1

    def top(self) -> int:
        if self.l==-1:
            return null
        return self.stack[self.l]

    def getMin(self) -> int:
        #store index/l value of previous min?
        return self.stack[self.cmin_index]
        