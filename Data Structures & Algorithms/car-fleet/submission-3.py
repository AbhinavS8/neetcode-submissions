class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #keep adding to the car fleet as long as
        # it can reach target before car in front
        # but its not sorted??

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        # li=[]
        fleets=0
        if len(pairs)==0:
            return 0
        if len(pairs)==1:
            return 1
        
        # print(pairs)
        c_time=-1

        for p,s in pairs:
            time = (target-p)/s
            # print(time)

            if time<=c_time:
                pass
            else:
                print("new fleet")
                c_time=time
                fleets+=1
        
        # if 
        return fleets





