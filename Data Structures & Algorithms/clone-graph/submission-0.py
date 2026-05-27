"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def cloneNode(oldNode):
            if not oldNode:
                return None

            newNode = Node(oldNode.val)
            seen[oldNode.val] = newNode

            for neighbor in oldNode.neighbors:
                if neighbor.val in seen:
                    newNode.neighbors.append(seen[neighbor.val])
                else:
                    newNode.neighbors.append(cloneNode(neighbor))

            return newNode
        return cloneNode(node)