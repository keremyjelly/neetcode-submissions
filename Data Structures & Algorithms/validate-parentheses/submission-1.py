class Solution:
    def isValid(self, s: str) -> bool:
        opener = set()
        opener.update('(', '{', '[')
        key = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
            }

        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            if c in opener:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif key[c] != stack.pop(-1):
                    return False
        return not stack
