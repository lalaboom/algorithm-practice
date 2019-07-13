

#enumerate() 函数用于将一个可遍历的数据对象
# (如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

solution1: 暴力解法
def two_sum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i, m in enumerate(nums):
        j = i+1
        while j < length:
            if target == (m+nums[j]):
                return [i, j]
            else:
                j = j+1

solution2: 字典模拟Hash
def two_sum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i , m in enumerate(nums):
        dict[m] = i
    for i, m in enumerate(nums):
        j = dict.get(target - m)
        if not j and i != j:
            return [i,j]

