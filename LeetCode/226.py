class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        # 交换左右子树
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root