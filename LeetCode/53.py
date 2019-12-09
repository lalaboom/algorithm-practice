cur_sum = 0
res = num[0]
n = len(nums)
for i in range(n):
    if (cur_sum>0):
        cur_sum+=nums[i]
    else:
        cur_sum = num[i]
    res = max(res,cur_sum)
return res