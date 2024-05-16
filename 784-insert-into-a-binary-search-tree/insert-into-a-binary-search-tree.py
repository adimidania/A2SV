# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        child = parent = root
        while child:
            parent = child
            if val > child.val:
                child = child.right
            else:
                child = child.left
        
        new_node = TreeNode(val)
        if val > parent.val:
            parent.right = new_node
        else:
            parent.left = new_node
        
        return root