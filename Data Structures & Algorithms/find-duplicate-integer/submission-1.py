class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # easy soln, hash and check
        st = set()

        for i in nums:
            if i in st:
                return i
            else:
                st.add(i)
        