class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" : return 0
        l, r = 0, 1
        seen = set(s[l])
        maxl = 1
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen and l < r:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            maxl = max(maxl, len(seen))
            r += 1
            
        return maxl