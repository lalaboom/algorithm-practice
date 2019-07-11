# 输入一个整数数组，
# 判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。
# 假设输入的数组的任意两个数字都互不相同。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not len(sequence):
            return False
        if len(sequence)==1:
            return True
        length = len(sequence)
        root = sequence[-1] #根节点
        i = 0
        while sequence[i] < root:
            i = i+1
        k = i
        for j in range(i,length-1):
            if sequence[j]<root:
                return False
        left_s = sequence[:k]
        right_s = sequence[k:length-1]
        left, right = True, True
        if len(left_s) > 0:
            left = self.VerifySquenceOfBST(left_s)
        if len(right_s) > 0:
            right = self.VerifySquenceOfBST(right_s)
        return left and right
        







