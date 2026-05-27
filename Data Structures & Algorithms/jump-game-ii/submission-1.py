class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        currPos = 0
        moves = 1

        while currPos < len(nums):
            jumpLength = nums[currPos]

            if jumpLength + currPos >= len(nums) - 1:
                break

            currMax = 0
            nextPos = currPos
            for i in range(1, jumpLength + 1):
                
                if nums[currPos + i] >= currMax:
                    currMax = nums[currPos + i]
                    nextPos = currPos + i
            
            currPos = nextPos
            moves += 1

        return moves