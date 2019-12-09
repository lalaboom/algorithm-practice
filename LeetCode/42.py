length = len(nums)
if length<2:
    return 0
cur_max_index = nums[0]
pre_max_index = nums[0]
res = 0+1
for i in range(1,length):
    if cur_max_index < i:
        cur_max_index = pre_max_max_index
        res += 1
    if pre_max_max_index < nums[i] + i:
        pre_max_max_index =  nums[i] + i
return res

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        cur_max_index = nums[0]
        pre_max_max_index = nums[0]
        res = 1
        for i in range(length):
            if cur_max_index < i:
                cur_max_index = pre_max_max_index
                res += 1
            if pre_max_max_index < nums[i] + i:
                pre_max_max_index =  nums[i] + i
        return res

作者：aofengli
链接：https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-2-by-aofengli/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。