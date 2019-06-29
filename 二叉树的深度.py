# 题目：二叉树的深度
# 输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
# 最长路径的长度为树的深度。
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0

        leftCount = self.TreeDepth(pRoot.left)+1
        rightCount = self.TreeDepth(pRoot.right)+1
        x= max(leftCount, rightCount)
        return x