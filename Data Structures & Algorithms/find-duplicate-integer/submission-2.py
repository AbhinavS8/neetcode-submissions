class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # easy soln, hash and check
        st = set()

        # for i in nums:
        #     if i in st:
        #         return i
        #     else:
        #         st.add(i)
        
        # for O(1) space.. could just sort and check for repeating nos
        # increases runtime to O(n log n)
        # but shouldn't modify input array, so won't work

        # using index?

        index = 0
        temp = 0

        for i in range(len(nums)+1):

            if nums[index] == -1:
                return index
            
            temp = nums[index]
            nums[index] = -1

            index = temp


