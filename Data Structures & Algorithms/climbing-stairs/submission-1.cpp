class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3)
        {
            return n;
        }

        // Base case - where n = 3
        // i.e. when n = 1, 1 way to climb, when n = 2, 2 ways to climb
        int nMinusTwo = 1;
        int nMinusOne = 2;
        int nCurr;

        for (int i = 2; i < n; i++)
        {
            // To reach n:
            //      Can either take two steps from n-2 or one step from n-2
            nCurr = nMinusTwo + nMinusOne;
            nMinusTwo = nMinusOne;
            nMinusOne = nCurr;
        }

        return nCurr;
    }
};
