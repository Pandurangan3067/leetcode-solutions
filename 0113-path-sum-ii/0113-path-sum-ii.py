# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def dfs(node, curr):
            if not node:
                return
            if not node.left and not node.right:
                if sum(curr) + node.val == targetSum:
                    ans.append(curr + [node.val])
                return
            curr.append(node.val)
            dfs(node.left, curr)
            dfs(node.right, curr)
            curr.pop()
        dfs(root, [])
        return ans