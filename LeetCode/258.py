class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        while(len(num)>1):
            tmp=0
            for a in num:
                tmp+=int(a)
            tmp=str(tmp)
            num=tmp
        return int(num)
#O（1）所要用的数学归纳法不够容易理解