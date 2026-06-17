class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        currMin = nums[0]

        while l <= r:
            mid = (l + r) // 2
            midVal = nums[mid]

            if midVal >= currMin:
                ## Middle is larger than current min, so discard everything to the left
                l = mid + 1
            else:
                ## Smaller value found, so discard everything to the right
                r = mid - 1

                currMin = midVal
        
        return currMin
