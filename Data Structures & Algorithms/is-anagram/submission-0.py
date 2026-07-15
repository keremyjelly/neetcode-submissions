class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = dict()
        counts_t = dict()

        for l in s:
            counts_s[l] = counts_s.get(l, 0) + 1
        for c in t:
            counts_t[c] = counts_t.get(c, 0) + 1
        return (counts_s == counts_t)