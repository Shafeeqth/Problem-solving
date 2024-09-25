class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
                continue 
            while stack and stack[-1] > 0:
                
                if stack[-1] < abs(x):
                    stack.pop()
                elif stack[-1] == abs(x):
                    stack.pop()
                    break
                else:
                    break 
            else:
                 stack.append(x)

        return stack

        