

#enumerate() 函数用于将一个可遍历的数据对象


def lengthOfLongestSubstring(self, s):
    count = 0
    start = 0
    end = 0
    WindowSet = set()
    while start< len(s) and end<len(s):
        WindowLnegth = len(WindowSet)
        WindowSet.add(s[end])
        if not WindowLnegth == len(WindowSet):
            end += 1
            count = max(count, end- start)
        else:
            WindowSet.remove(s[start])
            start +=1
    return count



