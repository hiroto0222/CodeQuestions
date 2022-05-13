from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root_tree, sub_tree):
            if not root_tree and not sub_tree:
                return True
            elif not root_tree or not sub_tree or root_tree.val != sub_tree.val:
                return False
            return dfs(root_tree.left, sub_tree.left) and dfs(root_tree.right, sub_tree.right)
        
        q = deque()
        q.append(root)
        while q:
            head = q.popleft()
            if head.val == subRoot.val:
                if dfs(head, subRoot):
                    return True
            
            if head.left:
                q.append(head.left)
            if head.right:
                q.append(head.right)
        
        return False