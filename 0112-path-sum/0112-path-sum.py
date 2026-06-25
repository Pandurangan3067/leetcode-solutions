# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,c):
            if not root:
                return False
            c+=root.val
            if not root.left and not root.right:
                return c==targetSum
            return dfs(root.left, c) or dfs(root.right,c)
        return dfs(root,0)
        