#二叉树中和为某一值的路径

# 题目：

# 输入一颗二叉树的跟节点和一个整数，
# 打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的
# 结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)

# # 思路：

# 深度优先搜索。使用前序遍历，使用两个全局变量result和tmp，result来存放最终结果，tmp用来存放临时结果。

# 每次遍历，我们先把root的值压入tmp，然后判断当前root是否同时满足：

# 与给定数值相减为0；
# 左子树为空；
# 右子树为空。
# 如果满足条件，就将tmp压入result中，
# 否则，依次遍历左右子树。需要注意的是，遍历左右子树的时候，
# 全局变量tmp是不清空的，直到到了根结点才请空tmp。

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return [] #如果根节点为空，返回空
        if not root.left and not root.right and expectNumber = root.val:
            return [[root.val]] #如果左子树和右子树都没有，并且符合计数，则返回此数值
        res = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)  
        for i in left+right:
            res.append([root.val]+i)
        return res  
