


# 设置两指针i,j分别位于容器壁两端，逐渐向中间收缩并记录最大值；
# 每次选定围成水槽两板height[i], height[j]中较小的对应指针，向中间收缩，这是因为：
# 水槽的高度由两板中的短板决定，每次收缩，都会导致水槽底边宽度-1，
# 因此，若想找到比当前最大值更大的水槽，那么水槽的短板高必须要高于上一个水槽短板高，
# 而只有向内移动短板，有可能达成这一条件（若移动长板，下个水槽的面积一定小于当前水槽面积）。




class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res= 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res








