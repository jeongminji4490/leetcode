# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, node: TreeNode, visited: List[int]):
        if node.left is not None:
            self.visit(node.left, visited)
        if node.right is not None:
            self.visit(node.right, visited)

        visited.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []

        if root is not None:
            self.visit(root, visited)

        return visited