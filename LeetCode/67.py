class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        # print(d)
        a = '0' * d + a
        b = '0' * -d + b
        # print(a)
        # print(b)
        for i, j in zip(a[::-1], b[::-1]):

            s = int(i) + int(j) + p
            # print(s)
            r = str(s % 2) + r
            # print(2)
            p = s // 2
        return '1' + r if p else r