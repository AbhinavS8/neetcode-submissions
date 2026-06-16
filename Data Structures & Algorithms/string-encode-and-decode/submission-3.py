class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            s+=st+"\0"
        
        return s

    def decode(self, s: str) -> List[str]:
        if s=="\0":
            return [""]
        return s.split("\0")[:-1]