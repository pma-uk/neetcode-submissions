# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Get slow pointer to second half
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        head2 = slow.next
        slow.next = None
        prev = None

        while head2 is not None:
            temp = head2.next
            head2.next = prev
            prev = head2

            head2 = temp

        head2 = prev

        # Merge
        head1 = head
        while head1:
            temp1 = head1.next
            head1.next = head2
            head1 = temp1

            if head2:
                temp2 = head2.next
                head2.next = temp1
                head2 = temp2

        return