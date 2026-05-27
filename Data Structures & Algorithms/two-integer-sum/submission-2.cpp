class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seenMap;
        int reqNum;

        for (int i = 0; i < nums.size(); i++)
        {
            reqNum = target - nums[i];
            if (seenMap.find(reqNum) != seenMap.end())
            {
                return {seenMap[reqNum], i};
            }

            seenMap.insert(make_pair(nums[i], i));
        }

        return {};
    }
};
