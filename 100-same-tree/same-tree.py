# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return [None]
            else:
                return [root.val] + traversal(root.left) + traversal(root.right) 
        return traversal(q) == traversal(p)
        