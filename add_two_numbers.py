# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lhs = ''
        rhs = ''

        while l1:
            lhs += str(l1.val)
            l1 = l1.next
        while l2:
            rhs += str(l2.val)
            l2 = l2.next

        sum = int(lhs[::-1]) + int(rhs[::-1])
        sum = str(sum)[::-1]

        sumList = ListNode()

        head = sumList

        for i, el in enumerate(sum):
            sumList.val = el
            if i + 1 < len(sum):
                sumList.next = ListNode()
            sumList = sumList.next

        return head
