## 孩子们的游戏(圆圈中最后剩下的数)
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n<1 or m <1:
            return -1
        last = 0
        people = range(n)
        i = 0
        for num in range (n , 1, -1):
            i = (i+m-1)%num
            people.pop(i)
        return people[-1]


        # write code here
        
        







