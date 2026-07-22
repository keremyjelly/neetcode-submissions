class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxheight = 0
        for l in range(len(heights) - 1):
            for r in range(l + 1, len(heights)):
                a = min(heights[l],heights[r]) * (r - l)
                if a > maxheight:
                    maxheight = a
        return maxheight

                