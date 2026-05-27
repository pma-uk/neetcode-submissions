class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getTimeToTarget(pos, sp):
            return (target - pos) / sp
        
        cars = sorted(zip(position, speed), reverse=True)
        #print(cars)
        
        stack = []

        # From car closest to target to furthest
        for pos, sp in cars:
            stack.append(getTimeToTarget(pos, sp))
            #print(stack)

            # If car in next (lower) position gets to target faster, then its part of the same fleet
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                #print("popped")
                stack.pop()

        return len(stack)

