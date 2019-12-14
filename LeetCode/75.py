	def sortColors(self, nums):
        #参考题解中的荷兰国旗问题值得再看
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		if not nums or len(nums)==0:
			return
		i = 0
		# 第一次遍历数组，处理所有0元素，将他们放到合适的位置
		# j指针不断往前走，如果指向的的元素==0，就交换i，j指向的元素
		for j in range(len(nums)):
			if nums[j]==0:
				nums[j],nums[i] = nums[i],nums[j]
				i += 1
		# 这里有一个优化，j不用重头开始遍历了，第一次遍历完之后i前面的元素都已经排好序了
		# 所以直接从i开始遍历就可以了
		for j in range(i,len(nums)):
			if nums[j]==1:
				nums[j],nums[i] = nums[i],nums[j]
				i += 1