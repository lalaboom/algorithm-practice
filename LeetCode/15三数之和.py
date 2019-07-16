


	# 取整除 - 返回商的整数部分


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n,res = len(nums),[]
        for i in range(n):
            #首位数字只要>0,就一定不会有合理的组合
            if nums[i] > 0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue 
            left,right = i+1,n-1
            while left < right:
                cum = nums[i] + nums[left] + nums[right]
                if cum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left+1] == nums[left]:
                        left += 1
                    while left<right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cum < 0:
                    left += 1
                else:
                    right -= 1
        return res








