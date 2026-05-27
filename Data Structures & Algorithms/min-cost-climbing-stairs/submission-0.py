class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        goalIndex = len(cost)
        cost.append(0) # Add 0 for goal

        # cost to get to n = 1 and n = 2 are base cases

        nMinus2 = nMinus1 = 0

        #cost to get to n from n - 2 or n - 1 = min(cost to get to n - 2 + cost of n - 2, cost to get to n - 1 + cost of n - 1)

        for n in range(2, goalIndex + 1):
            currentCost = min(nMinus2 + cost[n-2], nMinus1 + cost[n-1])
            nMinus2 = nMinus1
            nMinus1 = currentCost

        return nMinus1