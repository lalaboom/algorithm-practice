class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.res = float("-inf")
        def helper(root):
            if not root: return 0
            # 右边最大值
            left = helper(root.left)
            # 左边最大值
            right = helper(root.right)
            # 不经过根节点的结果和res相比较
            self.res = max(left + right + root.val, self.res)
            # >0 说明都能使路径变大，即使能变大也不一定是最后的结果，结果主要还是上一句
            return max(0, max(left,  right) + root.val)
        helper(root)
        return self.res 