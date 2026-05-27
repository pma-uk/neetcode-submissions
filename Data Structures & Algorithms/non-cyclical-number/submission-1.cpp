class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seenSet;

        while (n != 1)
        {
            if (seenSet.find(n) != seenSet.end())
            {
                return false;
            }

            seenSet.insert(n);
            n = sumSquaredDigits(n);
        }

        return true;
    }

    int sumSquaredDigits(int num)
    {
        int divisor = 1000;
        int sum = 0;
        int digit; 

        while (divisor >= 1)
        {
            digit = num / divisor;
            num = num % divisor;

            sum += pow(digit, 2);

            divisor /= 10;
        }

        return sum;
    }
};
