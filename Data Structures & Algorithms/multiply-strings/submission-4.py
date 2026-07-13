class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        l1,l2 = len(num1), len(num2)
        rowpad = 0
        for i in range(l1-1,-1,-1):
            intpad = 0
            for k in range(l2-1,-1,-1):
                res += int(num1[i]) * int(num2[k]) * 10**(rowpad + intpad)
                intpad += 1
            rowpad += 1
        return str(res)