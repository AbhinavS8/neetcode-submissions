class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # temp = 0
        # if a>b:
        #     temp = a
        #     a = b
        #     b = temp

        # sm = 0
        # carry = 0
        # bit = 0
        # i = 0

        # while b!=0:
        #     lsba = a & 1
        #     lsbb = b & 1

        #     bit = carry ^ lsba ^ lsbb
            
        #     if carry == 0:
        #         carry = lsba & lsbb
        #     else:
                
        #         carry = lsba | lsbb
            
        #     a = a >> 1
        #     b = b >> 1
        #     sm = sm | (bit << i)
        #     i+=1
        
        # if carry:
        #     sm = sm | (1 << i)
        
        # return sm


        # need to handle negative numbers as well!
        # remember adder formulas

        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res