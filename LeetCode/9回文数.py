


# 首先，考虑双指针法，但int类型无法遍历每一位，转化为str需要额外空间，不符合题意；
# 其次，考虑数字反转，若反转后数字==原数字，则为回文；
# 本解采用半倒置，即只取数字后一半并反转，判断前后两部分是否相等：
# 返回 x == r or x == r // 10：数字位数有奇偶区别，当为奇数时，r可能比x多一位。
# x % 10 == 0要直接返回false：以上方法无法判断XX0这类数字（会返回True），例如10, 20等等，其实XX0肯定不是回文数，因为数字最高位不可能为0；
# x < 0直接返回false。

// :取整除 - 返回商的整数部分（向下取整）
% : 取模，返回商的余数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or not x % 10 and x: return False
        r = 0
        while x > r:
            x, rem = x // 10, x % 10
            r = r * 10 + rem
        return x == r or x == r // 10






