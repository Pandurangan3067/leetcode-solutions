# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []

        def dfs(node, curr):
            if not node:
                return ""
            if not node.left and not node.right:
                
                ans.append(curr+str(node.val))
                return
            curr+=str(node.val)+"->"
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, "")
        return ans