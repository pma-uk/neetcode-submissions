class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        integerLocDict = {}

        for i in range(len(nums)):
            curr = nums[i]

            diff = target - curr
            if diff in integerLocDict:
                return [integerLocDict[diff], i]

            integerLocDict[curr] = i

        return []