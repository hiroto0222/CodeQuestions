# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode], lst: list):
        if not root: return
        self.inOrderTraversal(root.left, lst)
        lst.append(root.val)
        self.inOrderTraversal(root.right, lst)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.inOrderTraversal(root, ans)
        for i in range(len(ans) - 1):
            if ans[i] >= ans[i + 1]:
                return False
        return True