# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy

        a = l1
        b = l2
        carry = 0

        while a or b:
            val1 = a.val if a else 0
            val2 = b.val if b else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

            if a:
                a = a.next

            if b:
                b = b.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next