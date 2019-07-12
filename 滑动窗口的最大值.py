#给定一个数组和滑动窗口的大小，
# 找出所有滑动窗口里数值的最大值。
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0:
            return []
        res = []
        for i in range(0, len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res

        
        







