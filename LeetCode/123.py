class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0
        
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
            
        return second_sell
'''
这个系列的题真是折磨人呐。首先还是要先确定需要记录几个状态值。

对于某一天来说，可能会发生的情况：

第一次被买入
第一次被卖出
第二次被买入
第二次被卖出
按题目要求，我们最重要求出的是第二次被卖出所能获得的最大收益。

我们分别用 4 个变量来表示这 4 种情况下所能获得的最大收益：

在某天完成第一次买入的最大收益 first_buy
在某天完成第一次被卖出的最大收益 first_sell
在某天完成第二次被买入的最大收益 second_buy
在某天完成第二次被卖出最大收益 second_sell
可以得出状态转移公式：

first_buy = max(first_buy, -price)
first_sell = max(first_sell, first_buy + price)
second_buy = max(second_buy, first_sell - price)
second_sell = max(second_sell, second_buy + price)
其中 price 为某天股票的价格。

作者：jalan
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/4-ge-zhuang-tai-zhi-qiu-jie-by-jalan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


'''
补充动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        k = 2
        n = len(prices)
        dp = [[[0 for i in range(2)] for i in range(k+1)] for i in range(n)]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        for i in range(1,n):
            for j in range(1,3):
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]
————————————————
版权声明：本文为CSDN博主「乖乖的函数」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ggdhs/article/details/92618827
'''