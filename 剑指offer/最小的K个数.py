# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，
# 则最小的4个数字是1,2,3,4,。

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return
        n = len(tinput)
        if n < k:
            return []
        tinput = sorted(tinput)
        return tinput[:k]
            

        
        







