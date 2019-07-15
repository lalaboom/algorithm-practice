




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            n = len(nums1)
            n = int(n/2)
            mid = (nums1[n-1] + nums1[n])/2
            return mid
        elif len(nums1) %2 != 0:
            s = int((len(nums1)+1)/2 -1)
            return nums1[s]



