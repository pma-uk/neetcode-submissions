class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getTimeToTarget(pos, sp):
            return (target - pos) / sp
        
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []

        # From car furthest from target to closest
        for pos, sp in cars:
            stack.append(getTimeToTarget(pos, sp))

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

