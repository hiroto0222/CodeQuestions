# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inOrderTraversal(self, root, lst):
        if not root: return
        self.inOrderTraversal(root.left, lst)
        lst.append(root.val)
        self.inOrderTraversal(root.right, lst)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lst = []
        self.inOrderTraversal(root, lst)
        for i in range(1, len(lst)):
            if lst[i - 1] >= lst[i]:
                return False

        return True 