class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 对k进行求余
        k %= len(nums)
        nums[:] = nums[-k:] + nums[0:-k]