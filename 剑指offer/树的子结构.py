
# 题目:树的子结构

# 思路：
# 要查找树A中是否存在和树B结构一样的子树，
# 我们可以分为两步：第一步在树A中找到和B的根结点的值一样的结点R，
# 第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。
# 这里使用递归的方法即可。

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2) or self.isSubtree(pRoot1,pRoot2)
    def isSubtree(self,A,B):
        if not B:
            return True
        if not A or B.val != A.val:
            return False
        return self.isSubtree(A.left, B.left) and self.isSubtree(A.right, B.right)