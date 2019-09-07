def rotate(nums, k):
    # 对k进行求余
    print(len(nums))
    print('-------')
    k %= len(nums)
    print(k)
    print('-------')
    print(nums[-k:])
    print('-------')
    print(nums[0:-k])
    nums[:] = nums[-k:] + nums[0:-k]
    print('-------')
    print(nums)
    
nums1, nums2 = [1,2,3,4,5,6,7], [1,2,3,4,5,6,7]
rotate(nums1, 3)
#rotate(nums2, 23)
