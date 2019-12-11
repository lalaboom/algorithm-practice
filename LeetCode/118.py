class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[[0]*n for n in range(1,numRows+1)] 
        for row in range(numRows):
            dp[row][0]=dp[row][-1]=1
        for row in range(0,numRows):
            for col in range(i+1):
                if(dp[row][col]==0):
                    dp[row][col]=dp[row-1][col-1]+dp[row-1][col]
        return dp


'''
边界全为1，不为1的位置dp[i][j]=dp[i-1][j-1]+dp[i-1][j]dp[i][j]=dp[i−1][j−1]+dp[i−1][j]

模拟法（动态规划）
初始化结果数组，numRowsnumRows表示结果数组dpdp的行数，每一行的元素个数等于所处第几行。全部初始化为0
将边界全部初始化为1
遍历dpdp，将为00的位置使用动态规划填入，公式：dp[i][j]=dp[i-1][j-1]+dp[i-1][j]dp[i][j]=dp[i−1][j−1]+dp[i−1][j]
'''