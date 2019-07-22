


	# 取整除 - 返回商的整数部分



class Solution(object):
    def isValid(self, s):
        stack= []
        mapping = {")":"(","}":"{","]":"["}
        for char in s:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack










