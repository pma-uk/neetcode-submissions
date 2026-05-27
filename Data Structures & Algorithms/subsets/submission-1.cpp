class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;

        dfs(0, nums, result, subset);

        return result;
    }

    void dfs(int index, const vector<int> &nums, vector<vector<int>> &result, vector<int> &subset)
    {
        if (index >= nums.size())
        {
            result.push_back(subset);
            return;
        }

        subset.push_back(nums[index]);
        dfs(index+1, nums, result, subset);
        subset.pop_back();
        dfs(index+1, nums, result, subset);

        return;
    }
};
