# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.order = []
        self.inorderRecursive(root)
        return self.order

    def inorderRecursive(self, root):
        if root:
            self.inorderRecursive(root.left)
            self.order.append(root.val)
            self.inorderRecursive(root.right)
        