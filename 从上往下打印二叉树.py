#从上往下打印二叉树

# 题目：

#从上往下打印出二叉树的每个节点，同层节点从左至右打印。

# 思路：

#遍历二叉树的两种方式：
# 1.递归
# 2.非递归，入栈：根节点入栈，如果节点不为空，处理这个节点，同时左右子节点入栈

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        temp = [root]
        result = []
        while len(temp):
            cur = temp.pop(0)
            result.append(cur.val)
            if cur.left:
                temp.append(cur.left)
            if cur.right:
                temp.append(cur.right)
        return result