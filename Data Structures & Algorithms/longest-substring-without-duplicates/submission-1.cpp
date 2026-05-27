class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seenSet;
        int maxLength = 0;
        int front = 0;

        for (int back = 0; back < s.size(); back++)
        {
            while (seenSet.find(s[back]) != seenSet.end())
            {
                seenSet.erase(s[front]);
                front++;
            }

            seenSet.insert(s[back]);
            maxLength = max(maxLength, back - front + 1);
        }
        

        return maxLength;
    }
};
