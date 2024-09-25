class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            while x < 0  and stack and stack[-1] > 0:
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

        