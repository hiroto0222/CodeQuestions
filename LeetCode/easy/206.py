# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # recursive
    def reverseListRecur(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        newHead = head
        if (head.next):
            newHead = self.reverseListRecur(head.next)
            head.next.next = head
        head.next = None
        
        return newHead

    def reverseListIter(self, head: ListNode):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
