class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i]= nums[i] , nums[j]
                j += 1


        """
        Do not return anything, modify nums in-place instead.
        """
#         i = 0,1,2,3
#         j = 0,1
        
#         0,1,2,3,4
#         3,0,0,4,5
        