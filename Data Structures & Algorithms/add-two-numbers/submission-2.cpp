/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Digits stored in reverse order, so already in appropriate order to
        // add digits one by one

        ListNode* currL1 = l1;
        ListNode* currL2 = l2;
        ListNode* resultPreHead = new ListNode(0, nullptr);
        ListNode* currResult = resultPreHead;

        int sum = 0;
        int remainder = 0;

        while (currL1 != nullptr || currL2 != nullptr)
        {
            sum = remainder;
            if (currL1 != nullptr) 
            {
                sum += currL1->val;
                currL1 = currL1->next;
            }

            if (currL2 != nullptr)
            {
                sum += currL2->val;
                currL2 = currL2->next;
            }

            // Set result
            int currDigit = sum % 10;
            currResult->next = new ListNode(currDigit, nullptr);

            // Set new remainder
            if (sum > 9)
            {
                remainder = sum / 10;
            }
            else
            {
                remainder = 0;
            }

            // Prep next
            currResult = currResult->next;

            //Check if both lists are null - if yes, check if last digit exists
            if (currL1 == nullptr && currL2 == nullptr)
            {
                if (remainder > 0) 
                {
                    currResult->next = new ListNode(remainder, nullptr);
                }
            }
        }



        return resultPreHead->next;
    }
};
