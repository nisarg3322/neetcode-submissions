from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        stack = deque()

        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2:
                first_car_time = stack.pop()
                if first_car_time > stack[-1]:
                    stack.append(first_car_time)

        
        return len(stack)
