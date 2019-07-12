# 字符串的排列
# # 题目：

# 输入一个字符串,
# 按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能
# 排列出来的所有字符串abc,acb,bac,bca,cab和cba。

# # 思路：

# a = set('abracadabra')
# 运行：
# a                                  
# {'a', 'r', 'b', 'c', 'd'}

#Python join() 方法
# 用于将序列中的元素以指定的字符连接生成一个新的字符串

# map(function, iterable, ...)

#Python中的itertools.permutations:
# 返回可迭代对象的所有数学全排列方式。

# -*- coding:utf-8 -*-
import itertools
class Solution:
    # s 源字符串
    def Permutation(self, ss):
        if ss == '':
            return []
        return sorted(list(map(''.join,set(itertools.permutations(list(ss))))))
      
            
      






