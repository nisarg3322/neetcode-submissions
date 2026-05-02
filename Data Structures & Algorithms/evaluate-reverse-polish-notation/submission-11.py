from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        elif len(tokens) == 0:
            return 0
        stack = deque()
        operator = set(['+', '-', '*', '/'])

        for t in tokens:
            if t == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif t == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif t == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif t == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                r = int(b/a)
                stack.append(r)
            else:
                stack.append(int(t))
            
            
        return stack.pop()