class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seenMap;
        vector<int> results;
        int reqNum;

        for (int i = 0; i < nums.size(); i++)
        {
            reqNum = target - nums[i];
            if (seenMap.find(reqNum) != seenMap.end())
            {
                results.push_back(seenMap[reqNum]);
                results.push_back(i);
                return results;
            }

            seenMap.insert(make_pair(nums[i], i));
        }

        return results;
    }
};
