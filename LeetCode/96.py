#卡特兰数问题
class Solution:
    def numTrees(self, n: int) -> int:
        if(n==0):
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[-1]

# 作者：zhu_shi_fu
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/qia-te-lan-shu-dong-tai-gui-hua-python3-by-zhu_shi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。