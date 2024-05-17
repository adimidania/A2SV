# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = [root]
        output = [root.val]
    
        while queue:
            subarr = []    
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)

                if node.right:
                    queue.append(node.right)
                    subarr.append(node.right.val)
                
                if node.left:
                    queue.append(node.left)
                    subarr.append(node.left.val)
            
            if subarr:
                output = subarr
        
        return output[-1]