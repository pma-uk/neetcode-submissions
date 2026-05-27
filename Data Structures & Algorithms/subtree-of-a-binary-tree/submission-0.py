# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSubtree(node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not node and not subRoot:
                return True
            
            if not node or not subRoot or node.val != subRoot.val:
                return False

            return checkSubtree(node.left, subRoot.left) and checkSubtree(node.right, subRoot.right)

        if not subRoot:
            return True
        
        if not root:
            return False

        if root.val == subRoot.val and checkSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)