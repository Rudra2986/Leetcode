# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        temp = slow.next
        slow.next = None

        prev = None

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        # Merge two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        return head
