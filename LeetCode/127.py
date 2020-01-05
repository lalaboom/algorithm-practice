class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len1=len(s)
        len2=len(t)
        dp=[[1]*(len1+1)]+[[0]*(len1+1) for _ in range(len2)]
        for i in range(1,len2+1):
            for j in range(1,len1+1):
                if(t[i-1]==s[j-1]):
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]

# 作者：zhu_shi_fu
# 链接：https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。