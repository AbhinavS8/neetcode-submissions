class TimeMap:

    # first hash for each key
    # then hash self.tmap[key][0] under each key?

    def __init__(self):
        
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.tmap:
            self.tmap[key] = [[timestamp],[value]]
        else:
            self.tmap[key][0].append(timestamp)
            self.tmap[key][1].append(value)


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.tmap:
            return ""
        
            
        # binary search

        r = len(self.tmap[key][0]) -1
        l = 0
        # print("timestamp and key:",timestamp,key)

        while l<=r:
            m = l + (r-l)//2
            if self.tmap[key][0][m]==timestamp:
                return self.tmap[key][1][m]
            
            elif self.tmap[key][0][m]<timestamp:
                l = m+1
            
            else:
                r = m-1
            
            # print(l,r,m,self.tmap[key][0])
        
        else:
            m = r
            # print(m)
            if m <= timestamp and m>=0:
                return self.tmap[key][1][m]
            return ""
        




        # normal search is too inefficient!

        # for i in range(len(keys)-1,-1,-1):
        
        # for i in keys[::-1]:
        #     if keys[i]<=timestamp:
        #         return self.tmap[key][keys[i]]



