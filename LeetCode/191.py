class Solution:
    def hammingWeight(self, n: int) -> int:
        #十进制转二进制，统计1
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count