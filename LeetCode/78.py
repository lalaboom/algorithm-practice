class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def huisu(index,temp_value):
            res.append(temp_value)
            for j in range(index,n):
                huisu(j+1,temp_value+[nums[j]])
            # return res
        huisu(0,[])
        return res