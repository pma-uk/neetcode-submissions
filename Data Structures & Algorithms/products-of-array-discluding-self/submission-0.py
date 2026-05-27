class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # From left to right, get product rolling product for elements to the left of current index
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        # Now from right to left
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            result[i] *= product

        return result


        