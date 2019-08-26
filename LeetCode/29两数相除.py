# 除法的意义：被除数中包含了多少个除数
# 但我们可以对减数进行倍增操作。对于dividend，如果dividend - divisor > 0，那么我们下一次减去的数不是divisor，而是divisor + divisor，这样倍增减数的操作可以使我们的时间复杂度到达O(log(dividend / divisor))的级别。而空间复杂度依然保持O(1)的级别

# 假设divisor + divisor * 2 + divisor * 2 ^ 2 + divisor * 2 ^ 3 + ... + divisor * 2 ^ n = dividend。那么我们总共只进行了n次操作，这个时间复杂度显然就是O(log(dividend / divisor))。而如果divisor + divisor * 2 + divisor * 2 ^ 2 + divisor * 2 ^ 3 + ... + divisor * 2 ^ n > dividend，但是divisor + divisor * 2 + divisor * 2 ^ 2 + divisor * 2 ^ 3 + ... + divisor * 2 ^ (n - 1) < dividend，那么我们就要以dividend - (divisor + divisor * 2 + divisor * 2 ^ 2 + divisor * 2 ^ 3 + ... + divisor * 2 ^ (n - 1))为被减数进行重复的操作，即从divisor开始减起。直至我们的被减数小于divisor为止

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0: # 为了个最后的数字添加符号
            tag = 1
        else: 
            tag = -1
        dividend = abs(dividend)
        divisor = abs(divisor) # 全都变为正数

        if dividend < divisor:
            return 0
        
        returnNum = 0 # 返回结果
        while dividend >= divisor:
            index = 1 # 存储商的
            temp = divisor
            while temp + temp <= dividend:
                temp += temp
                index += index
            returnNum += index
            dividend -= temp
return max(min(res_value, 2*10**31-1), -2*10**31)