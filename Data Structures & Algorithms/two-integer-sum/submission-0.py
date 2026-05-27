class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seenDict = {}

        for i, num in enumerate(nums):
            requiredVal = target - num
            if requiredVal in seenDict:
                return [seenDict[requiredVal], i]
            
            seenDict[num] = i
        
        return []