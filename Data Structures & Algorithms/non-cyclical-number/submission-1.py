class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            nstr = str(n)
            sum = 0
            for digit in nstr:
                sum += int(digit)**2
            if sum == 1:
                return True
            elif sum in seen:
                break
            seen.add(sum)
            n = sum
        return False