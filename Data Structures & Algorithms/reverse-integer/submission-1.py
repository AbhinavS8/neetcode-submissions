class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        if x==0:
            return 0
     
        if x>0:
            res = int(str(x)[::-1])
        else:
            res = -int(str(x)[:0:-1])

        if res<=MIN or res>=MAX:
            return 0
        else:
            return res

