class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = dict()
        for i in nums:
            map[i] = map.get(i,0)+1
        for key, val in map.items():
            if val == 1:
                return key

