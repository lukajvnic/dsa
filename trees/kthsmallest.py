# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, node, k, count):
        res = None

        if node.left is not None:
            count, res = self.search(node.left, k, count)
        
        if res is not None:
            return count, res

        print(node.val, count)
        count += 1
        if count == k:
            return count, node.val

        if node.right is not None:
            count, res = self.search(node.right, k, count)
        
        return count, res


    def kthSmallest(self, root, k: int) -> int:
        return self.search(root, k, 0)[1]


# test = TreeNode(
#         5,
#         TreeNode(
#             3,
#             TreeNode(2, TreeNode(1, None, None), None),
#             TreeNode(4, None, None)
#         ),
#         TreeNode(
#             6,
#             None,
#             None
#         )
#     )

test = TreeNode(
        4,
        TreeNode(3, TreeNode(2), None),
        TreeNode(5)
    )

sol = Solution()
print(sol.kthSmallest(test, 4))
