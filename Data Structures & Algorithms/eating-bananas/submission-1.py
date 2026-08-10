class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink, maxk = 1, max(piles)
        res = maxk
        while mink <= maxk:
            mid = (mink + maxk) // 2
            hours = 0
            for p in piles:
              hours += math.ceil(p / mid)
        
            if hours <= h:
                res = min(res, mid)
                maxk = mid - 1
            else:
                mink = mid + 1
        return res