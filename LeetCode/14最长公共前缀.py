


	# 取整除 - 返回商的整数部分




class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res









