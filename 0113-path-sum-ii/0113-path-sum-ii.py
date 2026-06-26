class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, c, l):
            if not node:
                return c
            
            # Create a new list for the current path instead of mutating 'l' in place
            current_path = l + [node.val]
            
            if not node.left and not node.right:
                if sum(current_path) == targetSum:
                    c.append(current_path)
                return c
            
            # Because 'c' is passed by reference, it acts as a global accumulator.
            # We don't need to use '+' to combine returns. Just call the branches.
            dfs(node.left, c, current_path)
            dfs(node.right, c, current_path)
            
            return c
            
        return dfs(root, [], [])