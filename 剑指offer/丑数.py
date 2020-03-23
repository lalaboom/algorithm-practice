## 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 
# 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        baselist = [1]
        min2, min3, min5 = 0, 0 ,0 #找到初始的没有乘2，或3，或5的数
        CurIndex = 1
        while CurIndex < index:
            MinNum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(MinNum)
            while baselist[min2]*2 <= MinNum:
                min2 +=1
            while baselist[min3]*3 <= MinNum:
                min3 +=1
            while baselist[min5]*5 <= MinNum:
                min5 +=1
            CurIndex += 1
        return baselist[-1]


    
        
        

      
        
        







