class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> results(n + 1);
        int offset = 1;

        for (int i = 1; i <= n; i++)
        {
            if (offset * 2 == i)
            {
                offset = i;
            }
            results[i] = results[i - offset] + 1;
        }

        return results;
    }

};
