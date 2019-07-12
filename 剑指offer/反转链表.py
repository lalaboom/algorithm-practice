#反转链表

# 题目：

# 输入一个链表，反转链表后，输出新链表的表头。

# 思路：

# 链表的题画图能更直观明了一些

# 更改链表头，更改链表next指向

# 简单来说就是，让它指向下一个，让下一个指向它

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        next_pointer = None
        while pHead:
            temp = pHead.next
            pHead.next = next_pointer
            next_pointer = pHead
            pHead = temp
        return next_pointer