# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First get length of LL
        currNode = head

        length = 0

        while currNode:
            length += 1
            currNode = currNode.next

        # The node to remove
        toRemove = length - n

        prevNode = None
        currNode = head
        # navigate to the node to be removed
        while toRemove > 0:
            prevNode = currNode
            currNode = currNode.next
            toRemove -= 1

        # If prevNode is none, then head is being removed
        if not prevNode:
            return currNode.next

        # Remove node
        prevNode.next = currNode.next
        return head

