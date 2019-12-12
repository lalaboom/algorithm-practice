class MyQueue:
    #区分peek和pop的区别，一个是返回首元素，一个是移除首元素
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.stack = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        tmp_stack = []
        while self.stack:
            tmp_stack.append(self.stack.pop())
        self.stack.append(x)
        while tmp_stack:
            self.stack.append(tmp_stack.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack: return self.stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack: return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.stack)