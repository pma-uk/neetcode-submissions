class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > 0) break; // Break if current/leftmost value is > 0 - no more triplets
            if (i > 0 && nums[i] == nums[i-1]) continue; // Continue if current value is same as previous

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum > 0) right--;
                else if (sum < 0) left++;
                else
                {
                    result.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left-1])
                    {
                        left++;
                    }
                }
            }


        }

        return result;
    }
};
