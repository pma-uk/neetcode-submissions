class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(currIndex, currSum):
            if currSum == target:
                result.append(subset.copy())
                return
            if currIndex >= len(nums) or currSum > target:
                return

            subset.append(nums[currIndex])

            newSum = currSum + nums[currIndex]

            dfs(currIndex, newSum)
            subset.pop()
            dfs(currIndex + 1, currSum)

        dfs(0, 0)
        return result