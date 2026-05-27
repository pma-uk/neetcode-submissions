class MinStack
{
private:
    std::stack<int> fullStack;
    std::stack<int> minStack;
public:
    MinStack() 
    {}

    void push(int val)
    {
        if (minStack.empty() || minStack.top() >= val)
        {
            minStack.push(val);
        }

        fullStack.push(val);
    }

    void pop()
    {
        if (fullStack.empty()) return;

        if (minStack.top() == fullStack.top()) minStack.pop();

        fullStack.pop();
    }

    int top()
    {
        return fullStack.top();
    }

    int getMin()
    {
        return minStack.top();
    }
};