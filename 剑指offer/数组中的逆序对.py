## 数组中的逆序对
#在数组中的两个数字，
# 如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 
# 即输出P%1000000007
class Solution:
    def InversePairs(self, data):
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007


    
        
        

      
        
        







