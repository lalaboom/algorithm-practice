class Solution:

    def permute(self, nums):
        if len(nums) == 0:
            return []

        used = [False] * len(nums)
        res = []
        index = 0
        self.__dfs(nums, index, [], used, res)
        return res

    def __dfs(self, nums, index, pre, used, res):
        # 先写递归终止条件
        if index == len(nums) and pre not in res:
            res.append(pre.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                # 如果没有用过，就用它
                used[i] = True
                pre.append(nums[i])

                # 在 dfs 前后，代码是对称的
                self.__dfs(nums, index + 1, pre, used, res)

                used[i] = False
                pre.pop()
class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []

        # 修改 1：首先排序，之后才有可能发现重复分支，升序、倒序均可
        nums.sort()
        # nums.sort(reverse=True)

        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res

#     def __dfs(self, nums, index, pre, used, res):
#         if index == len(nums):
#             res.append(pre.copy())
#             return
#         for i in range(len(nums)):
#             if not used[i]:
#                 # 修改 2：因为排序以后重复的数一定不会出现在开始，故 i > 0
#                 # 和之前的数相等，并且之前的数还未使用过，只有出现这种情况，才会出现相同分支
#                 # 这种情况跳过即可
#                 if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
#                     continue
#                 used[i] = True
#                 pre.append(nums[i])
#                 self.__dfs(nums, index + 1, pre, used, res)
#                 used[i] = False
#                 pre.pop()

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。