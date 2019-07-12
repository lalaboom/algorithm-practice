# 按之字形顺序打印二叉树

# # 题目：

# 请实现一个函数按照之字形打印二叉树，
# 即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，
# 第三行按照从左到右的顺序打印，其他行以此类推。

# # 思路：

#第一层从左到右，二层从右到左，依次反转，设置标志符判断是否反转 


class Solution:
    def Print(self, pRoot):
        root = pRoot
        if not root:
            return []
        level = [root]
        result = []
        lefttoright = False
        while level:
            curvalues = []
            nextlevel = []
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if lefttoright:
                curvalues.reverse()
            if curvalues:
                result.append(curvalues)
            level = nextlevel
            lefttoright = not lefttoright
        return result






