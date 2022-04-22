# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ans = False
        seen = set()
        self.dfs(root, ans, seen, k)
        return ans


    def dfs(self, node: TreeNode, ans: bool, seen: set, k: int):
        if not node:
            return
        
        self.dfs(node.left, ans, seen, k)
        if node.val in seen:
            ans = True
        else:
            seen.add(k - node.val)
        self.dfs(node.right, ans, seen, k)


head = TreeNode(5)
head.left = TreeNode(3)
head.left.left = TreeNode(2)
head.left.right = TreeNode(4)

head.right = TreeNode(6)
head.right.right = TreeNode(7)

print(Solution().findTarget(head, 28))