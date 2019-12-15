class Solution:
    def rob(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        n=len(nums)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[-1]

# 作者：zhu_shi_fu
# 链接：https://leetcode-cn.com/problems/house-robber/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
