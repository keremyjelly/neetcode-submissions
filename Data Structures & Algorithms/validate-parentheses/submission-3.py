class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        key = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
            }

        for c in s:
            if c in key:
                if stack and stack[-1] == key[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return (not stack)
