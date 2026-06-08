# problem not found


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        s = 0
        que = [(root, 0)]
        while que:
            for _ in range(len(que)):
                node, is_left = que.pop(0)
                if not node.left and not node.right and is_left:
                    s += node.val

                node.left and que.append((node.left, 1))
                node.right and que.append((node.right, 0))

        return s
