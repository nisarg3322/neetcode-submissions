from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

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
            
            
        return int(stack.pop())