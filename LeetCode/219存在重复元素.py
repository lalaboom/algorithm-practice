class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 判断存在重复元素的索引之差小于某个数
        # 先判断 nums [i] = nums [j]
        # 然后判断索引值是否相等，所以索引值可以用 map 存起来
        length = len(nums)
        map = dict()
        if length == 0 :
            return False
        for i in range(length):
            if nums[i] in map & i - map[nums[i]] <=k:
                return True
            map[nums[i]] = i
        return False
