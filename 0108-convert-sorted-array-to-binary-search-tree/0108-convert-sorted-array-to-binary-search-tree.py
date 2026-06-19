# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start,end=0,len(nums)-1
        if start > end:
            return None

        mid = (start + end) // 2

        root =TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[start: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: end+1])

        return root

            