class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '.' + s for s in strs)

    
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.index('.', i)
            l = int(s[i:j])
            res.append(s[j + 1: j + 1 + l])
            i = j + 1 + l
        return res
