


	# 取整除 - 返回商的整数部分



class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans =set()
        for i in range (len(nums)-3):
            for j in range (i+1,len(nums)-2):
                left =j+1
                right = len(nums)-1
                while right > left :
                    temp = nums[i] + nums[j] +nums[left]+nums[right]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    if temp>target:right-=1#太大了，右指针左移
                    if temp<target:left+=1#反之
        return list(ans)
        
        rec=[]
        for i in ans:
            rec.append(list(i))
        return rec









