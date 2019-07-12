# 斐波那契数列

# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。

class Solution:
    def Fibonacci(self, n):
        if n<=1:
            return n
        first,second,third = 0,1,0
        for i in range(2,n+1):
            third = first +second
            first = second
            second = third
        return third
      






