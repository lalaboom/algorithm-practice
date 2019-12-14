class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = []
        n = len(nums)//2-1 if len(nums)%2==0 else len(nums)//2
        for i in set(nums):
            if nums.count(i)>n:
                # res.append(i)
                return i