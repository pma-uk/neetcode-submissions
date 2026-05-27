# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        # Take bottom-up approach
        # Max diameter will be at a node whose diameter is largest
        # Need to keep track of 2 things:
        #   1) current max diameter 
        #   2) current max height/depth at current node
        
        # Use depth first search since mostly looking for height/depth
        def dfs(node):
            nonlocal maxDiam # make sure that maxDiam is not local to dfs

            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            maxDiam = max(maxDiam, left + right) # Current max diameter   

            return max(left, right) + 1 # Current max height at node

        dfs(root)
        return maxDiam

