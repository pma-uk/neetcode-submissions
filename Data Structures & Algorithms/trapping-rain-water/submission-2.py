class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        areaSum = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                areaSum += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                areaSum += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
                
        return areaSum