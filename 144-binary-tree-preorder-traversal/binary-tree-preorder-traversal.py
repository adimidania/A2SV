# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.order = []
        self.preorderRecursive(root)
        return self.order

    def preorderRecursive(self, root):
        if root:
            self.order.append(root.val)
            self.preorderRecursive(root.left)
            self.preorderRecursive(root.right)
        