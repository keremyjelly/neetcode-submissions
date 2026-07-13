class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        l = len(s)
        for idx in range(l):
            total += self.countPali(s, idx, idx)
            total += self.countPali(s, idx, idx + 1)
        return total
            
    def countPali(self, s, l, r) -> bool:
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res