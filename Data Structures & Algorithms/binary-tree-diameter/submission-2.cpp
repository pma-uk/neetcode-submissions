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
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        depthFirstSearch(root, maxDiameter);
        return maxDiameter;
    }

    int depthFirstSearch(TreeNode* root, int& maxDiam)
    {
        if (root == nullptr)
        {
            return 0;
        }

        int leftDepth = depthFirstSearch(root->left, maxDiam);
        int rightDepth = depthFirstSearch(root->right, maxDiam);

        maxDiam = max(leftDepth + rightDepth, maxDiam);

        return max(leftDepth, rightDepth) + 1;
    }
};
