# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        prevNode = None
        currentNode = head

        while currentNode:
            # Store next node
            tempNode = currentNode.next

            # Overwrite next node
            currentNode.next = prevNode

            # Prepare next step
            prevNode = currentNode
            currentNode = tempNode

        return prevNode
