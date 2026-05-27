class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currGoal = len(nums)-1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= currGoal:
                currGoal = i
        
        return currGoal == 0

            
