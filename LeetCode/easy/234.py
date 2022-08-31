# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. get middle using 2 pointers
        # 2. reverse 2nd half
        # 3. check palindrome

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# print(Solution().isPalindrome())