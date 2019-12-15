class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n, y = divmod(n, 26)
            print(y) 
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res


# 作者：powcai
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-title/solution/shi-jin-zhi-zhuan-26jin-zhi-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。