# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal = True

        def height(node):
            if not node: return 0

            left = height(node.left)
            right = height(node.right)

            self.isBal =  self.isBal and abs(left - right) < 2

            return 1 + max(left, right)
        
        height(root)

        return self.isBal