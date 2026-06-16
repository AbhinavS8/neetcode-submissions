class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        finaldict={}
        for word in strs:
            st=[0,]*26

            for i in word:
                st[ord(i)-ord('a')]+=1

            st=tuple(st)
            if st in finaldict:
                finaldict[st].append(word)
            else:
                finaldict[st]=[word,]

        return list(finaldict.values())