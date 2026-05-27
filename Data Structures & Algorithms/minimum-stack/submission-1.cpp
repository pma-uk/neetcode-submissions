class MinStack {
public:
    stack<int> fullStack;
    stack<int> minStack;

    MinStack() {
        
    }
    
    void push(int val) {
        if (minStack.empty() || minStack.top() >= val)
        {
            minStack.push(val);
        }

        fullStack.push(val);
    }
    
    void pop() {
        if (fullStack.empty())
        {
            return;
        }

        if (fullStack.top() == minStack.top())
        {
            minStack.pop();
        }

        fullStack.pop();
    }
    
    int top() {
        return fullStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
