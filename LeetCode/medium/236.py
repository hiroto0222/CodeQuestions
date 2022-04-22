# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        # build a map of parents for each node; stop once we have found p, q
        stack = [root]
        parent = { root: None }
        while p not in parent or q not in parent:
            
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # build set of all of p's ancestors
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
            
        # traverse through q's ancestors, first one to appear in p's ancestors in the lowest common
        while q not in ancestors:
            q = parent[q]
        
        return q

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.left.left = None
root.left.left.right = None
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = TreeNode(5)
q = TreeNode(1)

ans = Solution().lowestCommonAncestor(root, p, q)
print(ans.val)