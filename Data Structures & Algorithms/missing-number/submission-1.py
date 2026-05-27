class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums) + 1):
            result += i
            if i < len(nums):
                result -= nums[i]

        return result