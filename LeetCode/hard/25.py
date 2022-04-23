# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prevNode, currNode = kth.next, groupPrev.next
            while currNode != groupNext:
                tmp = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = tmp

            tmp = groupPrev.next
            groupPrev.next = kth 
            groupPrev = tmp
        
        return dummy.next
    
    def getKth(self, currNode, k):
        while currNode and k > 0:
            currNode = currNode.next
            k -= 1
        return currNode


lst = [1, 2, 3, 4, 5]
head = ListNode(lst[0])
node = head
for i in range(1, len(lst)):
    node.next = ListNode(lst[i])
    node = node.next

print(Solution().reverseKGroup(head, 2))