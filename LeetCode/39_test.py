def Sum_Solution(n):
    ans = (n>0) and n
    print(ans)
    return ans and Sum_Solution(n-1)+ans
n=7
print(False+1)
