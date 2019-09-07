class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        k = len(nums)
        if k == 1:
            return False
        else:
            p = 0
            q = 1
            while q <= k-1:
                if nums[p] == nums[q]:
                    return True
                else:
                    p=q
                    q += 1 
            return False
        