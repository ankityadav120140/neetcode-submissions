# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            return max(left,right) + 1

        return (depth(root.left) - depth(root.right) in [-1,0,1])
        