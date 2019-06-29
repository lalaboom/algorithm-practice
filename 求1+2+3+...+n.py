
# 题目:求1+2+3+...+n

# 求1+2+3+...+n，要求不能使用乘除法、
# for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 思路：
#用递归

class Solution:
    def Sum_Solution(self, n):
        count = n
        if count:
            count = count + self.Sum_Solution(n-1)
        return count