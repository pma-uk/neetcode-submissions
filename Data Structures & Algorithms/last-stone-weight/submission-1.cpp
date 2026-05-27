class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        int larger, smaller;

        for (int stone: stones)
        {
            maxHeap.push(stone);
        } 

        while (maxHeap.size() > 1)
        {
            larger= maxHeap.top();
            maxHeap.pop();
            smaller = maxHeap.top();
            maxHeap.pop();

            if (larger > smaller)
            {
                maxHeap.push(larger - smaller);
            }
        }

        if (maxHeap.size() == 1)
        {
            return maxHeap.top();
        }

        return 0;


    }
};
