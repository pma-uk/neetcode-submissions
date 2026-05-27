class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0;
        int currMin = prices[0];
        int profit;

        for (int i = 1; i < prices.size(); i++)
        {
            maxP = max(maxP, prices[i] - currMin);

            if (prices[i] < currMin)
            {
                currMin = prices[i];
            }

        }


        return maxP;
    }
};
