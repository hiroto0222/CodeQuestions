from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(101)
        prevNode = dummyHead
        currNode = head
        duplicate = False
        
        while currNode.next:
            if currNode.val != currNode.next.val:
                if not duplicate:
                    prevNode.next = currNode
                    prevNode = currNode
                    currNode = currNode.next
                else:
                    currNode = currNode.next
                    duplicate = False
            else:
                currNode = currNode.next
                duplicate = True
        
        if not duplicate:
            prevNode.next = currNode
        
        return dummyHead.next


arr = [1,2,3,3,4,4,5]
head = ListNode(1)
node = head
for i in range(1, len(arr)):
    node.next = ListNode(arr[i])
    node = node.next

head.printList(head)

ans = Solution().deleteDuplicates(head)
ans.printList(ans)