class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            res.append((i >> 1) ^ i)

        # print((1^2))
        return res

# 直接背 二进制数转格雷码