class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases are when number of steps n is 1 or 2
        # (can include 3 since it's trivial)
        # Ways to make a staircase with
        #   n = 1: 1
        #   n = 2: 2
        #   n = 3: 3
        # For any n > 2, # of ways to make a staircase 
        # is to look at # ways to go from stairs of n - 2 
        # to n with 2 steps + # ways to go from stairs of n - 1
        # to n with 1 step

        if n < 3:
            return n

        nMinusTwo = 1
        nMinusOne = 2

        for i in range(3, n + 1):
            currentN = nMinusTwo + nMinusOne
            nMinusTwo = nMinusOne
            nMinusOne = currentN

        return nMinusOne