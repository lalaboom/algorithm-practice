
if len(height) ==0:
    return 0
left,right = 0,len(height)-1
left_max, right_max = height[left], height[right]
r= 0
while left < right:
     if height[left] <= height[right]:
        if height[left] > left_max:
            left_max = height[left]
        else:
            r += left_max - height[left]
        left += 1

    else:
        if height[right] > right_max:
            right_max = height[right]
        else:
            r += right_max - height[right]
        right -= 1

return r  