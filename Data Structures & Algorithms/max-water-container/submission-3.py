class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        
        left, right = 0, len(heights)-1

        while left < right:
            currentAmount = min(heights[left], heights[right]) * (right - left)
            currentMax = max(currentMax, currentAmount)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return currentMax