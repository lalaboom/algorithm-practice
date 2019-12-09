        dic = {}
        for s in strs:
            # print(s)
            # print(sorted(s))
            # print(tuple(sorted(s)))
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s] #等号前是key，后是dict的value
        return dic.values()

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            return 1/self.help_(x,n)
        return self.help_(x,n)

    def help_(self,x,n):
        if n==0:
            return 1
        if n%2 == 0:  #如果是偶数
            return self.help_(x*x, n//2)
        # 如果是奇数
        return self.help_(x*x,(n-1)//2)*x

x = 2
n = 5

return help(4,2)
help(4,2) = return help(16,1)
help(16,1) = return help(16*16,0)


