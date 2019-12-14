class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
	# 求高度
    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.right),self.height(node.left))
