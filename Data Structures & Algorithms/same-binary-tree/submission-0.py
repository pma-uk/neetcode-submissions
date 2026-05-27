# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not (p and q):
            return False
        
        pQueue = [p]
        qQueue = [q]

        while pQueue and qQueue:
            pNode = pQueue.pop(0)
            qNode = qQueue.pop(0)

            if pNode.val != qNode.val or bool(pNode.left) ^ bool(qNode.left) or bool(pNode.right) ^ bool(qNode.right):
                return False
            
            if pNode.left and qNode.left:
                pQueue.append(pNode.left)
                qQueue.append(qNode.left)
            
            if pNode.right and qNode.right:
                pQueue.append(pNode.right)
                qQueue.append(qNode.right)

        return True


