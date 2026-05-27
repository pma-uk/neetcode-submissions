class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> numsSet(nums.begin(), nums.end());
        if (nums.size() != numsSet.size())
        {
            return true;
        }

        return false;
    }
};
