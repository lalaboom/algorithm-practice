class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tl = len(s)
        stack = []
        st = 0
        maxlen = 0
        for i in range(tl):
            #如果是左括号，直接入stack
            if s[i] == '(':
                stack.append(i)
            #如果右括号
            else:
                #如果stack里没有元素匹对，说明有效括号已经结束，更新起始位置
                if len(stack) == 0:
                    st = i+1
                    continue
                #有元素匹对
                else:
                    a = stack.pop()
                    #pop出一个左括号匹对
                    #如果此时没了，不能保证不继续有效括号，所以根据当前的最长距离去更新maxlen
                    if len(stack) == 0:
                        maxlen = max(i - st+1, maxlen)
                    #如果此时还有 则计算与栈顶的索引相减来计算长度
                    else:
                        maxlen = max(i-stack[-1], maxlen)
 
        return maxlen