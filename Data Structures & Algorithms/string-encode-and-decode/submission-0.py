class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []
        
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            string = s[j + 1: j + length + 1]

            res.append(string)
            i = j + length + 1
        return res
        
