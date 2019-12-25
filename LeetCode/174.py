'''
自底向上，动态规划

'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        dp[-1][-1]=max(1,1-dungeon[-1][-1])
        for i in range(n-2,-1,-1):
            dp[-1][i]=max(1,dp[-1][i+1]-dungeon[-1][i])
        for i in range(m-2,-1,-1):
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]

# 作者：zhu_shi_fu
# 链接：https://leetcode-cn.com/problems/dungeon-game/solution/dong-tai-gui-hua-zi-di-xiang-shang-python3-by-zhu_/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。