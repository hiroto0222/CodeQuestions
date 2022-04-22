# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        currNode = dummyHead
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                currNode.next = list1
                currNode = list1
                list1 = list1.next
            else:
                currNode.next = list2
                currNode = list2
                list2 = list2.next
        
        currNode.next = list1 if list1 != None else list2
        return dummyHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)

        # cut the linked list in half
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeLists(left, right)
    


lst = [4, 2, 1, 3]
head = ListNode(lst[0])
node = head
for i in range(1, len(lst)):
    node.next = ListNode(lst[i])
    node = node.next

sortedHead = Solution().sortList(head)
while sortedHead:
    print(sortedHead.val)
    sortedHead = sortedHead.next