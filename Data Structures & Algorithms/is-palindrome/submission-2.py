class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ','')
        l, r = 0, len(s) - 1
        while l < r:
            print(s[l], s[r])
            while (l < r and not s[l].isalnum()):
                l += 1
            while (l < r and not s[r].isalnum()):
                r -= 1
            if l > r or s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True