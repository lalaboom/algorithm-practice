

if not nums:
    return 1
size = len(nums)
for i in range(size):
    while (0<nums[i]<=n and nums[i]!=nums[nums[i]-1]):
        nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
for i in range(size):
    if (nums[i]!=i+1):
        return i+1
return n+1
    
