# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 2 pointers
        slow = fast = head
        while head and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
