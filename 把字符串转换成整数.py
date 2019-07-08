# 把字符串转换成整数

# 将一个字符串转换成一个整数
# (实现Integer.valueOf(string)的功能，
# 但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 
# 数值为0或者字符串不是一个合法的数值则返回0。
# # 思路：
#float


class Solution:
    def StrToInt(self, s):
        try:
            return int(s)
        except:
            return 0
        # write code her
    
      






