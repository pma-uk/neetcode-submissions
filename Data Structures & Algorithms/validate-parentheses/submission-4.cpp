class Solution {
public:
    bool isValid(string s) {
        stack<char> bracketStack;
        char currBracket;

        for (int i = 0; i < s.size(); i++)
        {
            currBracket = s[i];

            switch(currBracket)
            {
                case ')':
                    if (bracketStack.size() == 0 || bracketStack.top() != '(')
                    {
                        return false;
                    }
                    bracketStack.pop();
                    break;
                case ']':
                    if (bracketStack.size() == 0 || bracketStack.top() != '[')
                    {
                        return false;
                    }
                    bracketStack.pop();
                    break;
                case '}':
                    if (bracketStack.size() == 0 || bracketStack.top() != '{')
                    {
                        return false;
                    }
                    bracketStack.pop();
                    break;
                default:
                    bracketStack.push(currBracket);
            }
        }

        if (bracketStack.size() != 0)
        {
            return false;
        }
        
        return true;
    }
};
