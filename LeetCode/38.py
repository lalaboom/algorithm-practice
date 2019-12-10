
#正常思维，从1开始到n层
def next_num(tmp):
    res = ""
    index = 0
    num_len = len(tmp)
    while index < num_len:
        count = 1
        while index < num_len-1 and tmp[index] == tmp[index+1]:
            count+=1
            index+=1
        res += (str(count)+tmp[i])
        i+=1
    return res
res = "1" #首字母
for i in range(1,n):
    res = next_num(res)
return res