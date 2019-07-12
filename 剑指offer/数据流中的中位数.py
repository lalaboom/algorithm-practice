## 如何得到一个数据流中的中位数？
# 如果从数据流中读出奇数个数值，
# 那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，
# 使用GetMedian()方法获取当前读取数据的中位数。
class Solution:
    def __init__(self):
        self.nums=[]
    def Insert(self, num):
        self.nums.append(num)
        self.nums.sort()
    def GetMedian(self,nums):
        length = len(self.nums)
        if length%2 == 1:
            return self.nums[length//2]
        else:
            return (self.nums[length//2-1]+self.nums[length//2])/2.0



        # write code here
        
        







