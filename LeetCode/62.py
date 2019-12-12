class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #动态规划：当前位置到达的方法取决于能达到这个位置的两个位置的方法
        #dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #但是需要对边界进行确定，即最上面一行和最左边一列每个位置只有一种方法能达到
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]