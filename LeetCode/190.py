class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        count = 32
        
        while count:
            res <<= 1
            # 取出 n 的最低位数加到 res 中
            res += n&1
            n >>= 1
            count -= 1
            
        return int(bin(res), 2)

# 作者：jalan
# 链接：https://leetcode-cn.com/problems/reverse-bits/solution/python-de-liang-chong-jie-fa-by-jalan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。