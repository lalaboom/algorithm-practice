#二分法不断缩小区间
        # 起始区间是[1, x]
        # x 在[1, x/2) [x/2, x)两个区间
        # 缩小区间直到[a b) b-a = 1
if x == 0:
    return 0
left = 1
right = x
while right -left >1:
    mid = (right+left)//2
    left.right = (left,mid) if mid*mid >x else (mid,right)
return left