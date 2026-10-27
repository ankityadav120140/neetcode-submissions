# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calMaxDepth(self, root: Optional[TreeNode],dep: int) -> int:
        if not root:
            return dep
        dep = max(self.calMaxDepth(root.left,dep + 1),self.calMaxDepth(root.right,dep + 1))
        return dep


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calMaxDepth(root,0)