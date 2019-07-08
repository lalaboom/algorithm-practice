# 第一个只出现一次的字符
# # 题目：

# 在一个字符串(0<=字符串长度<=10000，
# 全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

# # 思路：



# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        index = 0
        if s == "":
            return -1
        else:
            for i in s:
                if s.count(i) == 1:
                    return index
                index = index + 1
    
    
      






