# 包含min函数的栈

# 定义栈的数据结构，
# 请在该类型中实现一个能够得到栈中所含最小元素的min函数
# （时间复杂度应为O（1））。

# 思路：
# 使用两个stack，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据，辅助栈用于存储最小值。

# 举个例子：

# 入栈的时候：首先往空的数据栈里压入数字3，显然现在3是最小值，我们也把最小值压入辅助栈。接下来往数据栈里压入数字4。由于4大于之前的最小值，因此我们只要入数据栈，不压入辅助栈。

# 出栈的时候：当数据栈和辅助栈的栈顶元素相同的时候，辅助栈的栈顶元素出栈。否则，数据栈的栈顶元素出栈。

# 获得栈顶元素的时候：直接返回数据栈的栈顶元素。

# 栈最小元素：直接返回辅助栈的栈顶元素。
class Solution:
    def __init__(self):
        self.Data = []
        self.Min = []
    def push(self, node):
        if len(self.Min) == 0:
            self.Min.append(node)
        if self.Min[-1] > node:
            self.Min.append(node)
        self.Data.append(node)
        # write code here
    def pop(self):
        if self.Data[-1] == self.Min[-1]:
            self.Min.pop()
        self.Data.pop()
        # write code here
    def top(self):
        return self.Data[-1]
        # write code here
    def min(self):
        return self.Min[-1]
        # write code here
      






