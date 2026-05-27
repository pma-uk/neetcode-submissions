class Solution:
    def canJump(self, nums: List[int]) -> bool:
        toVisit = [0]

        if len(nums) <= 1:
            return True

        while toVisit:
            curr = toVisit.pop(0)

            for j in range(1, nums[curr] + 1):
                if curr + j == len(nums) - 1:
                    return True
                elif curr + j < len(nums):
                    toVisit.append(curr + j)
        
        return False

            
