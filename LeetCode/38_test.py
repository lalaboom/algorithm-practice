if not candidates:
    return []
n = len(candidates)
res = []
candidates.sort
def helper(i,tmp,target):
    if target==0:
        res.append(tmp)
        return
    if i == n or target<candidates[i]:
        return
    helper(i,tmp+[candidates[i]],target - candidates[i])
    helper(i+1,tmp,target)

helper(0,[],target)
return res