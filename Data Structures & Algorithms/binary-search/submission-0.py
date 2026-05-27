class Solution:
    def search(self, nums: List[int], target: int) -> int:
        resultIndex = -1

        currentLower = 0
        currentUpper = len(nums) - 1

        while currentLower <= currentUpper:
            midpoint = (currentLower + currentUpper) // 2

            if nums[midpoint] == target:
                return midpoint

            if target < nums[midpoint]:
                currentUpper = midpoint - 1
            else:
                currentLower = midpoint + 1

        return resultIndex