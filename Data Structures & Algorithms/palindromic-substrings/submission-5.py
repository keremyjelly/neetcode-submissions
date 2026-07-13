class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        l = len(s)
        for idx in range(l):
            for subidx in range(idx, l):
                total += self.isPalindrome(s[idx:subidx+1])
        return total

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]