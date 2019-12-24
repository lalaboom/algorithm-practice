
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        # print(sorted(map(str, nums), key=LargerNumKey))
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

# 假设（不是一般性），某一对整数 aa 和 bb ，我们的比较结果是 aa 应该在 bb 前面，这意味着 a\frown b > b\frown aa⌢b>b⌢a ，其中 \frown⌢ 表示连接
