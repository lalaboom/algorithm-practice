class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        max_l = self.maxDepth(root.left)  # 左子树的最大深度
        max_r = self.maxDepth(root.right) # 右子树的最大深度
        return max(max_l, max_r) + 1  