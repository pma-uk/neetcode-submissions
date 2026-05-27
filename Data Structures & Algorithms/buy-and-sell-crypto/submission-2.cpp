class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int currMin = prices[0];
        int profit;

        for (int i = 1; i < prices.size(); i++)
        {
            profit = prices[i] - currMin;
            if (profit > max)
            {
                max = profit;
            }

            if (prices[i] < currMin)
            {
                currMin = prices[i];
            }

        }


        return max;
    }
};
