class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> results;

        for (int i = 0; i <= n; i++)
        {
            results.push_back(getCount(i));
        }

        return results;
    }

    int getCount(int n)
    {
        int count = 0;

        while (n != 0)
        {
            if (n & 1 == 1)
            {
                count++;
            }

            n = n >> 1;
        }

        return count;
    }
};
