class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        vector<vector<int>> freqs(nums.size() + 1);
        vector<int> result;

        for (int num : nums)
        {
            counts[num]++;
        }

        for (auto [key, val] : counts)
        {
            freqs[val].push_back(key);
        }

        for (int i = freqs.size() - 1; i > 0; i--)
        {
            for (int val : freqs[i])
            {
                result.push_back(val);

                if (result.size() == k)
                {
                    return result;
                }
            }
        }

        return result;
    }
};
