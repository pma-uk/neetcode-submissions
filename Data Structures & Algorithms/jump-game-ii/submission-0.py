class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        currEnd = 0 # end of current jump
        jumps = 0 # number of jumps
        furthest = 0 # furthest reachable point

        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            # If reached end of current jump
            if i == currEnd:
                jumps += 1
                currEnd = furthest

                if currEnd >= len(nums) - 1:
                    break

        return jumps