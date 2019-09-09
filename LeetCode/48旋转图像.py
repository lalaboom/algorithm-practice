class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = matrix[::-1]
        #print(matrix)
        for i in range(0, n):
            for j in range(i+1, n):
                #print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/rotate-image/solution/yi-ci-xing-jiao-huan-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。