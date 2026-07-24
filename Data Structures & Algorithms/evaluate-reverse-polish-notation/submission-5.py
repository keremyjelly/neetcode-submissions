class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            print(stack)
            print(t)
            match t:
                case '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                case '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                case '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
                case '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case _:
                    stack.append(int(t))
        return int(stack.pop())

