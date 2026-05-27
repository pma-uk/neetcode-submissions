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
        int sum = 0;

        while (num > 0)
        {
            sum += (num % 10) * (num % 10);

            num /= 10;
        }

        return sum;
    }
};
