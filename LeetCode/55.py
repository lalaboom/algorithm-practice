class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        length=len(nums)
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
                if max_i>=length:
                    return True
        return max_i>=i

# 可能到达最远位置（贪心）。
# 如果能到达某个位置，那一定能到达它前面的所有位置。