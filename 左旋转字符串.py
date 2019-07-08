# 左旋转字符串

# 汇编语言中有一种移位指令叫做循环左移（ROL），
# 现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，
# 即“XYZdefabc”。是不是很简单？OK，搞定它！
# # 思路：
#float


class Solution:
    def LeftRotateString(self, s, n):
        length = len(s)
        if n<0 or length == 0:
            return s
        if n > length:
            n = n % length
        return s[n:] + s[:n]
    
      






