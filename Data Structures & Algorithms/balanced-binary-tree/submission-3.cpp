/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        bool balanced = true;

        dfs(root, balanced);
        return balanced;
    }

    int dfs(TreeNode* root, bool& balanced)
    {
        if (root == nullptr)
        {
            return 0;
        }

        int leftDepth = dfs(root->left, balanced);
        int rightDepth = dfs(root->right, balanced);

        balanced = balanced && abs(leftDepth - rightDepth) < 2;

        return max(leftDepth, rightDepth) + 1;
    }
};
