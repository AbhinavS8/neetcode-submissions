class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # maintain a set
        # can it be done in O(1) space?
        st = set()
        for i in nums:
            if i in st:
                return True
            else:
                st.add(i)

        return False