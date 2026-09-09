# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        new_root = TreeNode()
        
        if not root1: 
            new_root = root2

        if not root2:
            new_root = root1

        if not root1 and not root2:
            new_root = None

        if root1 and root2:
    
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)


            new_root.val = root1.val + root2.val

            new_root.left = left
            new_root.right = right

        return new_root
        

        