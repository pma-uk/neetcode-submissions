class Solution {
public:
    bool isPalindrome(string s) {
        int leftIndex = 0;
        int rightIndex = s.size() - 1;

        while(leftIndex < rightIndex)
        {
            while(!isalnum(s[leftIndex]) && leftIndex < rightIndex)
            {
                leftIndex++;
            }

            while(!isalnum(s[rightIndex]) && leftIndex < rightIndex)
            {
                rightIndex--;
            }
            
            if (tolower(s[leftIndex]) != tolower(s[rightIndex]))
            {
                return false;
            }
            
            leftIndex++;
            rightIndex--;
        }

        return true;
    }
};
