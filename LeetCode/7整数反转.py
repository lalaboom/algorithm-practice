




class Solution:
    def reverse(self, x: int) -> int:
        # 定义用来标记给定整数x的正负情况，若x>=0， 则flag=1；反之，则flag=-1
        flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        # 将abs(x)变成字符串
        x_str = str(abs_x)
        # 将字符串x_str反转
        reverse_x_str = x_str[::-1]
        # 最后恢复成整数
        reverse_x_int = int(reverse_x_str) * flag
        if -2 ** 31 <= reverse_x_int <= 2**31 - 1:
            return reverse_x_int
        else:
            return 0




