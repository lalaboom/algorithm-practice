#两个链表的第一个公共节点

# 题目：

# 输入两个链表，找出它们的第一个公共结点。

# 思路：

# 我们可以把两个链表拼接起来，一个pHead1在前pHead2在后，
# 一个pHead2在前pHead1在后。
# 这样，生成了两个相同长度的链表，那么我们只要同时遍历这两个表，
# 就一定能找到公共结点。
# 时间复杂度O(m+n)，空间复杂度O(m+n)。


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else pHead2
            cur2 = cur2.next if cur2 != None else pHead1
        return cur1