class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict()
        ans= []
        # if len(nums1) >= len(nums2):
        for i in nums1:
            if map.get(i) is None:
                map[i] = 1
            else:
                map[i] = map[i]+1
        for  j in nums2:
            if map.get(j) is not None :
                if map[j] >0:
                    ans.append(j)
                    map[j] = map[j]-1
        return ans
