# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque()
        q.append(root)
        dummy = Node(0)

        while q:
            prev = dummy  # store prev nodes on dummy to iterate next
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    prev.next = node.left
                    prev = prev.next
                if node.right:
                    q.append(node.right)
                    prev.next = node.right
                    prev = prev.next
        
        return root
    
    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root
        dummy = Node(0)
        head = root

        while head:
            curr = head
            prev = dummy

            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            
            head = dummy.next
            dummy.next = None
        
        return root



print(Solution().connect(root))