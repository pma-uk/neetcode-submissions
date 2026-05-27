class Solution {
public:
    bool canJump(vector<int>& nums) {
        int currGoal = nums.size() - 1;

        for (int i = nums.size() - 2; i > -1; i--)
        {
            if (i + nums[i] >= currGoal)
            {
                currGoal = i;
            }
        }

        return currGoal == 0;
    }
};
