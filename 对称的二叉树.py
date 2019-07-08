# 对称的二叉树

# # 题目：

# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，
# 如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# # 思路：

# 递归
class Solution:
    def isSymmetrical(self, pRoot):
        def is_same(p1,p2):
            if not(p1 or p2):
                return True
            elif p1 and p2 and p1.val == p2.val:
                return is_same(p1.left,p2.right) and is_same(p1.right,p2.left)
            return False
        if not pRoot:
            return True
        return is_same(pRoot.left,pRoot.right)  
