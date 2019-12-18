class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i-2]:
                nums[i] = n
                i += 1
        return i
#既然允许连个元素重复，那就从第三个元素开始遍历，每次比较第i个元素和第i-2个元素，如果相等就将第i个元素删掉，否则i+1