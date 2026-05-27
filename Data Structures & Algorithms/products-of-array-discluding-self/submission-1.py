class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Get cumulative product of all numbers to left of current index
        # starting at index 1
        curr_product = 1
        for i in range(1, len(nums)):
            curr_product = curr_product * nums[i - 1]
            result[i] = curr_product

        # Get cumulative product of all numbers to right of current index
        # starting at index before last
        curr_product = 1
        for i in range(len(nums) - 1, 0, -1):
            curr_product = curr_product * nums[i]
            result[i - 1] = result[i - 1] * curr_product

        return result
