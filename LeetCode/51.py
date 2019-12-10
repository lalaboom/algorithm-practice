class Solution:
    def solveNQueens(self, n):
        temp = [ ]
        cans = set(range(n))
        res = []

        def test(tl, x):
            l = len(tl)
            if l == 0:
                return True
            for i in range(l):
                if tl[i]-x == i-l or tl[i]-x == l-i:
                    return False
            return True

        def backtrack(temp, cans, res):
            if len(cans) == 0:
                res.append(temp[:])
                return res
            for loc in cans:
                if test(temp, loc):
                    temp.append(loc)
                    cans.remove(loc)
                    res =  backtrack(temp, cans, res)
                    cans.add(loc)
                    temp.pop()
            return res
        
        queenLocs = backtrack([], cans, [])
        for locs in queenLocs:
            locStr = [['.' for j in range(n)] for i in range(n)]
            for i in range(n):
                locStr[i][locs[i]] = 'Q'
                locStr[i] = ''.join(locStr[i])
            res.append(locStr)
        return res

作者：xu-fei
链接：https://leetcode-cn.com/problems/n-queens/solution/hui-su-fa-by-xu-fei/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。