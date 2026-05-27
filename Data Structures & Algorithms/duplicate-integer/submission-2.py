class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)

        if len(hashSet) < len(nums):
            return True

        return False