class Solution:
    def trap(self, height: List[int]) -> int:
        suffixes = [0] * len(height)
        prefixes = [0] * len(height)

        maxSuffix = 0
        for i in range(len(height) - 2, -1, -1):
            maxSuffix = max(height[i + 1], maxSuffix)
            suffixes[i] = maxSuffix

        maxPrefix = 0
        for i in range(1, len(height) - 1):
            maxPrefix = max(height[i - 1], maxPrefix)
            prefixes[i] = maxPrefix

        areaSum = 0
        for i in range(len(height)):
            areaSum += max(min(suffixes[i], prefixes[i]) - height[i], 0)

        return areaSum

