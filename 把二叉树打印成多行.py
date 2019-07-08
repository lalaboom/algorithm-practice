# 把二叉树打印成多行
# # 题目：

# 把二叉树打印成多行，从上到下按层打印二叉树，
# 同一层结点从左至右输出。每一层输出一行

# # 思路：

#第一层从左到右，二层从右到左，依次反转，设置标志符判断是否反转 


class Solution:
    def Print(self, pRoot):
        root = pRoot
        if not root:
            return []
        level = [root]
        result = []
        #lefttoright = False
        while level:
            curvalues = []
            nextlevel = []
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            # if lefttoright:
            #     curvalues.reverse()
            if curvalues:
                result.append(curvalues)
            level = nextlevel
            #lefttoright = not lefttoright
        return result






