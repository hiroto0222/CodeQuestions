"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self.preorderIterative(root)
    
    def preorderRecursive(self, root):
        if not root: return []
        ans = [root.val]
        for child in root.children:
            ans += self.preorder(child)
        return ans
    
    def preorderIterative(self, root: 'Node') -> List[int]:
        if not root: return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        
        return ans
            