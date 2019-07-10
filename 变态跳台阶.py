# 变态跳台阶
class Solution:
    def jumpFloorII(self, number):
        if number <= 0:
            return 0
        else:
            return pow(2,number-1)
            






