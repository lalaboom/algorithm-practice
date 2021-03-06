


	# 取整除 - 返回商的整数部分



        length = len(nums)
        res = []
        if length <3:
            return []
        diff = float('inf')
        nums.sort()
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = length -1
            while left <right:
                s= nums[i] + nums[left] + nums[right]
                if abs(s- diff)<diff:
                    diff = abs(s- target)
                    res= s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target

     
        # 特判
        if size < 3:
            return []
        # 初始化，因为找最小值，因此把初始值设置成实数的最大值
        diff = float('inf')

        # 排序是前提
        nums.sort()

        for i in range(size - 2):
            # 常见的剪枝操作
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针：指针对撞
            left = i + 1
            right = size - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s

                # 不管是变小还是变大，尝试的作用是让 s 与 target 更接近
                # 即 s 与 target 的绝对值之差越来越小
                if s > target:
                    # 如果大了，尝试右边界收缩一格，让 target 变小
                    right -= 1
                elif s < target:
                    # 如果小了，尝试左边界收缩一格，让 target 变大
                    left += 1
                else:
                    # 如果已经等于 target 的话, 肯定是最接近的，根据题目要求，返回这三个数的和
                    return target
        return res

                









