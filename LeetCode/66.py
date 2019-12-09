temp_add = 1
n = len(digits)
for i in range(n-1,-1,-1):
    if temp_add ==0:
        break
    if i == 0 and (digits[i]+temp_add==10):
        digits[i]=(digits[i]+temp_add)%10
        digits=[1]+digits
        continue
    cur=digits[i]+tmp
    digits[i]=cur%10
    tmp=cur//10
return digits