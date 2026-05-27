class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carryOver = 1; 
        int remainder;

        for (int i = digits.size()-1; i >= 0; i--)
        {
            digits[i] += carryOver;

            carryOver = digits[i] / 10;
            digits[i] = digits[i] % 10;

            if (carryOver == 0)
            {
                break;
            }
            else if (i == 0)
            {
                digits.insert(digits.begin(), carryOver);
            }
        }

        return digits;
    }
};
