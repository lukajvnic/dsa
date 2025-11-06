# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    out = []

    def traverse(self, t, depth):
        if len(self.out) < depth + 1:
            self.out.append([])

        self.out[depth] += [t.val]

        if t.left is not None:
            self.traverse(t.left, depth + 1)
        if t.right is not None:
            self.traverse(t.right, depth + 1)

    def levelOrder(self, root) -> list[list[int]]:
        if root is None:
            return []

        self.traverse(root, 0)
        return self.out

sol = Solution()
a = sol.levelOrder(
    TreeNode(1)
)
print(a)
