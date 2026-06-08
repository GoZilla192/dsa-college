# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target_sum, curr_sum):
        if not root:
            return False

        curr_sum += root.val
        if root.left is None and root.right is None:
            return curr_sum == target_sum

        return self.dfs(root.left, target_sum, curr_sum) or self.dfs(
            root.right, target_sum, curr_sum
        )

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.dfs(root, targetSum, 0)
