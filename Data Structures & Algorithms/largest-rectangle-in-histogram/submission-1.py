class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def updateStack(myStack: List[int], newVal: int) -> int:
            if not myStack:
                return newVal
            prev = myStack[-1]
            count = 0
            largest = prev

            # Pop from stack so long as values are larger than new value
            # Accumulate rectangles and keep track of max area
            while myStack and newVal < myStack[-1]:
                curr = myStack.pop()
                if prev > curr:
                    largest = max(largest, prev * count)

                count += 1
                #print(f"{prev} -> {curr} : {count}")
                prev = curr

            largest = max(largest, prev * count)
            # Fill stack back up with new value, if it isn't 0
            if newVal > 0:
                for _ in range(count):
                    myStack.append(newVal)
            return largest
                

        monoIncStack = []
        largest = 0
        heights.append(0) # This is for making sure all rectangles checked

        # First, iterate through rectangles, record largest seen
        # If current is smaller than previous, pop stack to maintain 
        # monotonically increasing elements while adding back at new val
        for height in heights:
            if monoIncStack and height < monoIncStack[-1]:
                largest = max(largest, updateStack(monoIncStack, height))
            monoIncStack.append(height)
            #print(f"{height} : {largest} : {monoIncStack}")

        # Get largest rectangle in remaining stack
        #largest = max(largest, updateStack(monoIncStack, 0))
        #print(monoIncStack)

        return largest