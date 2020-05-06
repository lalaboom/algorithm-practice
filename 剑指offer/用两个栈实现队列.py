# 用两个栈实现队列

# 用两个栈来实现一个队列，
# 完成队列的Push和Pop操作。
#  队列中的元素为int类型。
#栈是先进后出
#队列先进先出
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
      






