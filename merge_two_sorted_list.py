"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode()
        head = sorted_list
        
        while list1 and list2:

            if list1.val < list2.val:
                sorted_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                sorted_list.next = ListNode(list2.val)
                list2 = list2.next
                
            sorted_list = sorted_list.next
        
        while list1:
            sorted_list.next = ListNode(list1.val)
            list1 = list1.next
            sorted_list = sorted_list.next
        while list2:
            sorted_list.next = ListNode(list2.val)
            list2 = list2.next
            sorted_list = sorted_list.next
        
        return head.next
        









"""
Runtime: 51 ms, faster than 56.40% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 51.25% of Python3 online submissions for Merge Two Sorted Lists.
"""