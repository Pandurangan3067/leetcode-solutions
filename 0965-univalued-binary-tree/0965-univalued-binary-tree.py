# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, current):
            if not node:
                return True

            if node.val != current:
                return False
            
            return dfs(node.left, current) and dfs(node.right, current)

        return dfs(root, root.val)