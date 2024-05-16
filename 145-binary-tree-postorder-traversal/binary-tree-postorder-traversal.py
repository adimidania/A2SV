# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.order = []
        self.postorderRecursive(root)
        return self.order

    def postorderRecursive(self, root):
        if root:
            self.postorderRecursive(root.left)
            self.postorderRecursive(root.right)
            self.order.append(root.val)
        