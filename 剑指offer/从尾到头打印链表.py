#从尾到头打印链表

# 题目：

# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# 思路：

# 主要考察链表的基本知识，包括链表的节点Node，val，插入insert，位置（从0开始）

# 新建一个数组，把链表中的值不断从头插入即可

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result