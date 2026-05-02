from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        second_stack = deque()
        stack = deque()

        for temp in temperatures:
            stack.appendleft(temp)

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            x = stack.pop()
            count = 0
            while stack:
                if stack[-1] > x:
                    count += 1
                    result[i] = count
                    break
                else:
                    second_stack.append(stack.pop())
                    count += 1
            
            # while stack:
            #     num = stack.pop()
            #     count += 1
            #     second_stack.append(num)
            #     if num > x:
            #         result[i] = count
            #         break
            
            while second_stack:
                stack.append(second_stack.pop())

        return result
        