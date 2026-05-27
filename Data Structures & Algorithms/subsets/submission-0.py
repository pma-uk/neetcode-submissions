class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(currIndex):
            if currIndex >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[currIndex])
            dfs(currIndex + 1)
            subset.pop()
            dfs(currIndex + 1)

        dfs(0)

        return result

