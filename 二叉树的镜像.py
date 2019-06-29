# 题目：二叉树的镜像
# 操作给定的二叉树，将其变换为源二叉树的镜像。

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if (root == None or (root.left== None and root.right == None)):
            return None
        temp = root.right
        root.right = root.left
        root.left = temp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)