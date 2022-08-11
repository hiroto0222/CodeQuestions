# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        curr = head
        while list1 and list2:
            if (list1.val <= list2.val):
                curr.next = list1.val
                list1 = list1.next
            else:
                curr.next = list2.val
                list2 = list2.next

        if (not list1 and list2):
            curr.next = list2
        if (not list2 and list1):
            curr.next = list1

        return head.next
