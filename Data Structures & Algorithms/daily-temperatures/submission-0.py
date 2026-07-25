class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,c in enumerate(temperatures):
            print(i)
            while i - 1 >= 0 and stack and c > stack[-1][0]:
                t = stack.pop()
                res[t[-1]] = i - t[-1]
            stack.append((c, i))
        return res

