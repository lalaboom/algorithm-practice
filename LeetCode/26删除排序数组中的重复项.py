


	# 取整除 - 返回商的整数部分



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        p,q =0,1
        while q<len(nums):
            if nums[p] != nums[q]:
                nums[p+1] = nums[q]
                p += 1
                q += 1
            else:
                q+=1
        return p+1














