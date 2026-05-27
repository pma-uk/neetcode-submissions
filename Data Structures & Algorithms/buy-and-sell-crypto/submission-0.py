class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        currentBottom = prices[0]

        for i in range(1, len(prices)):
            if currentBottom > prices[i]:
                currentBottom = prices[i]
                continue
            
            currentProfit = prices[i] - currentBottom

            if currentProfit > maxProfit:
                maxProfit = currentProfit

        return maxProfit