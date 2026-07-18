class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            for c in s:
                code = code + str(ord(c) << 1) + '.'
            code = code + '\\'
        return code
    
    def decode(self, s: str) -> List[str]:
        decoded_s = []
        lines = s.split('\\')
        for l in lines:
            if not l:
                decoded_s.append("")
                continue
            print(l)
            d = ""
            bits = l.split('.')
            for b in bits:
                if not b:
                    continue
                print(b)
                d = d + chr(int(b) >> 1)
            decoded_s.append(d)
        decoded_s.pop(-1)
        return decoded_s
