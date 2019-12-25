# 从梯度下降或者上升的角度比较好理解
#通过二分法比较是上升还是下降不断逼近峰
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if(nums[mid]>nums[mid+1]):
                r=mid
            else:
                l=mid+1
        return l
