class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = dict()
        ans= []
        if len(nums1) >= len(nums2):
            for i in nums1:
                if map.get(i) is None:
                    map[i] =1
            for  j in nums2:
                if map.get(j) is not None:
                    ans.append(j)
                    map[j] = None
            return ans
        else:
            for i in nums2:
                if map.get(i) is None:
                    map[i] =1
            for  j in nums1:
                if map.get(j) is not None:
                    ans.append(j)
                    map[j] = None
            return ans
#直接返回return set(nums1)&set(nums2)也是一种做法
