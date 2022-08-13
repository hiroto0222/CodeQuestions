# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        
        return slow


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().detectCycle(head))
