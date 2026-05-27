"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        orig_node_dict = {}  # Holds node:index pairs
        copy_index_dict = {} # Holds index:node pairs

        orig_head = head
        copy_head = Node(orig_head.val)

        curr_copy_head = copy_head

        curr_index = 0
        orig_node_dict[orig_head] = curr_index
        copy_index_dict[curr_index] = curr_copy_head

        # First pass - just go in normal order, ignoring random index
        while (orig_head.next is not None):
            curr_index += 1

            # Create copy
            orig_head = orig_head.next
            curr_copy_head.next = Node(orig_head.val)
            curr_copy_head = curr_copy_head.next

            # Record indexes
            orig_node_dict[orig_head] = curr_index
            copy_index_dict[curr_index] = curr_copy_head

        # Second pass to get randoms
        # Only traverse original - keep one pointer on main path
        # and a second one to traverse random
        orig_head = head
        
        while orig_head is not None:
            # If random points to null, just continue
            if orig_head.random is None:
                orig_head = orig_head.next
                continue

            # Current copy index
            copy_index = orig_node_dict[orig_head]

            # Get random index
            rand_node = orig_head.random
            rand_index = orig_node_dict[rand_node]
            
            # Set random for copy
            copy_node = copy_index_dict[copy_index]
            copy_node.random = copy_index_dict[rand_index]

            # Continue
            orig_head = orig_head.next

        return copy_head




