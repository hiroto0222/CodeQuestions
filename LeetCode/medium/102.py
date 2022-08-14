# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = [[root.val]]
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                curr = q.popleft()
                if (curr.left):
                    temp.append(curr.left.val)
                    q.append(curr.left)
                if (curr.right):
                    temp.append(curr.right.val)
                    q.append(curr.right)
            if (temp):
                ans.append(temp)
        
        return ans